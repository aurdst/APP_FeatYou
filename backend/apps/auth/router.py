from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, Security, status
from apps.users.schemas import UserInDB, UserAuthSchema
from apps.users.models import UserModel
from database.database import get_db
from .tools import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from sqlalchemy.orm import Session
from datetime import timedelta

router: APIRouter = APIRouter()

# OAuth2PasswordRequestFormest une dépendance de classe qui déclare un corps de formulaire avec username et password
@router.post(
    path="/token",
    summary="Authenticate Access Token"
    )
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    userdb = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    user = authenticate_user(userdb, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}