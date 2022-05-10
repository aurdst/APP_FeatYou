from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from apps.auth.tools import get_current_user
from database.database import get_db
from typing import List
from apps.auth.tools import pwd_context
from passlib.context import CryptContext
from apps.users.schemas import UserAuthSchema
from fastapi.responses import Response
from apps.auth.schemas import Log

from . import models
from . import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router: APIRouter = APIRouter()

#Route for create a user
@router.post(
    path="/user/",
    response_model=schemas.UserSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create new user"
)
def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    datas = models.UserModel(
        firstName       = user.firstName,
        lastName        = user.lastName,
        username        = user.username,
        isadmin         = user.isadmin,
        phone           = user.phone,
        email           = user.email,
        hashed_password = pwd_context.hash(user.hashed_password),
        postalCode      = user.postalCode,
        banqCardNumb    = user.banqCardNumb,
        dateRegister    = user.dateRegister,
        adress          = user.adress
    )

    query = db.query(models.UserModel).filter(models.UserModel.email == datas.email).first() 
    if query:
        raise HTTPException(status_code=409, detail="user already exist")
    
    db.add(datas)
    db.commit()
    db.refresh(datas)
    
    return datas

#Create a get all user
@router.get(
    path="/user/get_all",
    response_model=List[schemas.UserViewSchema],
    summary="Get all user"
)
def get_all_user(db: Session = Depends(get_db), user: Log = Depends(get_current_user)):
    query = db.query(models.UserModel).all()
    return query

# Create a get routes for get one user in the db.
@router.get(
    "/user/{user_id}/", 
    response_model=List[schemas.UserViewSchema],
    summary="Get user by id"
)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(models.UserModel.id).filter(id == user_id)
    if not user:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    return user

# Route for update one user
@router.put(
    path="/user/update/{user_id}",
    response_model=schemas.UserSchema,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update user by id"
)
def update_user(user_id: str, update_user: schemas.UserSchema, db: Session = Depends(get_db), user: Log = Depends(get_current_user)):
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
@router.delete(
    path="user/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user by id",
    response_class=Response
)
def delete_user_by_id(user_id: str, db: Session = Depends(get_db), user: Log = Depends(get_current_user)):
    query = db.query(models.UserModel).filter(models.UserModel.id == user_id).delete()

    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    db.commit()