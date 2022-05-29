from http.client import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, Security, status
from sqlalchemy.orm import Session
from apps.users.schemas import UserAuthSchema, UserInDB, UserSchema
from apps.auth.schemas import TokenData
from apps.users.models import UserModel
from database.database import get_db
from typing import Optional
from datetime import datetime, timedelta

#* Security
from passlib.context import CryptContext
from jose import JWTError, jwt

#* to get a string like this run:
#* into the cmd go to : -> c:\ Program Files\ OpenSSL-Win64\ bin and run :
#* openssl rand -hex 32
SECRET_KEY = "891f3561c61fabf5dc401d15d6730986902b1e92e6e5be20f5567ebf358cd7db"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#* OAuth2 security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

#* Create a PassLib "context". This is what will be used to hash and verify passwords.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#* Pour la sécurité nous créons une fonction utilitaire pour hacher un mot de passe provenant de l'utilisateur.
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#* Permet de hasher un mot de passe
def get_password_hash(password):
    return pwd_context.hash(password)

#* Récupère l'utilisateur
def get_user(db: Session, username: str):
    user = db.query(UserModel).filter(username == UserModel.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

#*  Et un autre utilitaire pour vérifier si un mot de passe reçu correspond au hachage stocké.
def authenticate_user(username: str, password: str, db: Session):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user

#* Créez une fonction utilitaire pour générer un nouveau jeton d'accès.
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

#* Récupère l'utilisateur en cours
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
        
    return user

#* Check si l'user est actif
async def get_current_active_user(current_user: UserSchema = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user