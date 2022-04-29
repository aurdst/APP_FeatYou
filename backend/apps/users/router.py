from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List
from apps.auth.tools import pwd_context
from passlib.context import CryptContext
from apps.users.schemas import UserAuthSchema

from . import models
from . import schemas


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router: APIRouter = APIRouter()

#Route for create a user
@router.post("/user/", response_model=schemas.UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    datas = models.UserModel(
        firstName = user.firstName,
        lastName = user.lastName,
        username = user.username,
        isadmin = user.isadmin,
        phone = user.phone,
        email = user.email,
        hashed_password = pwd_context.hash(user.hashed_password),
        postalCode = user.postalCode,
        banqCardNumb = user.banqCardNumb,
        dateRegister = user.dateRegister,
        adress = user.adress
    )

    query = db.query(models.UserModel).filter(models.UserModel.email == datas.email).first() 
    if query:
        raise HTTPException(status_code=409, detail="user already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all user
@router.get("/user/get_all", response_model=List[schemas.UserViewSchema])
def get_all_user(db: Session = Depends(get_db)):
    query = db.query(models.UserModel).all()
    return query

# Create a get routes for get one user in the db.
@router.get("/user/{user_id}/", response_model=List[schemas.UserViewSchema])
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(models.UserModel.id).filter(id == user_id)
    if not user:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    return user

# Route for update one user
@router.put("/user/update/{user_id}", response_model=schemas.UserSchema, status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: str, update_user: schemas.UserSchema, db: Session = Depends(get_db)):
    query = db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    update_data = models.UserModel(
        labelCategorie = update_user.labelCategorie,
        descCategorie = update_user.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted user
@router.delete("user/{user_id}")
def delete_categorie_by_id(user_id: str, db: Session = Depends(get_db)):
    query = db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")
    else:
        db.delete(query)
    
    return query