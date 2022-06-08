from fastapi import APIRouter, Depends, status, HTTPException, UploadFile
from sqlalchemy.orm import Session
from apps.auth.tools import get_current_user
from database.database import get_db
from typing import List
from apps.auth.tools import pwd_context, authenticate_user
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from fastapi.responses import Response
from apps.auth.schemas import Log

from . import models
from . import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router: APIRouter = APIRouter()

#* Route for create a user
@router.post(
    path="/create",
    # response_model=schemas.UserSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create new user"
)
def create_user(user: schemas.UserCreateSchema, db: Session = Depends(get_db)):
    datas = models.UserModel(
        firstName       = user.firstName,
        lastName        = user.lastName,
        username        = user.username,
        isadmin         = False,
        iscoach         = user.iscoach,
        phone           = user.phone,
        email           = user.mail,
        hashed_password = pwd_context.hash(user.hashed_password),
        postalCode      = user.postalCode,
        banqCardNumb    = 0000000000000000,
        dateRegister    = user.dateRegister,
        adress          = user.adress,
        sport           = user.sports,
        lieux           = user.lieux,
        pict            = '',
        coin            = 0
    )

    query = db.query(models.UserModel).filter(models.UserModel.email == datas.email).first() 
    if query:
        raise HTTPException(status_code=409, detail="user already exist")

    db.add(datas)
    db.commit()
    db.refresh(datas)

    return datas

#* Create a get all user
@router.get(
    path="/get_all",
    response_model=List[schemas.UserViewSchema],
    summary="Get all user"
)
def get_all_user(db: Session = Depends(get_db)):
    query = db.query(models.UserModel).all()
    return query

@router.get(
    path="/get_coachs",
    response_model=List[schemas.CoachUserSchema],
    summary="Get all coach"
)
def get_all_coach(db: Session = Depends(get_db)):
    return db.query(models.UserModel).filter(models.UserModel.iscoach == True).all()

@router.get(
    path="/coach/{coach_id}",
    response_model=schemas.CoachUserSchema,
    summary="Get coach"
)
def get_coach(coach_id: str, db: Session = Depends(get_db)):
    coach = db.query(models.UserModel).filter(models.UserModel.id == coach_id, models.UserModel.iscoach == True).first()
    
    if not coach:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    return coach

#* Create a get routes for get one user in the db.
@router.get(
    "/infos/{user_id}", 
    response_model=schemas.UserViewSchema,
    summary="Get user by id"
)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    return user

#* Route for update one user
@router.put(
    path="/update/{user_id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=schemas.UserSchema,
    summary="Update user by id"
)
def update_user(user_id: str, update_user: schemas.UpdateUserSchema, db: Session = Depends(get_db)):
    to_put = db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
    if not to_put:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    if update_user.new_password:
        if update_user.old_password:
            user = authenticate_user(to_put.username, update_user.old_password, db)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            user.hashed_password = pwd_context.hash(update_user.new_password),
        else :
            raise HTTPException(status_code=401, detail="Please enter your old password")
    else :
        user = to_put

    user.firstName  = update_user.firstName,
    user.lastName   = update_user.lastName,
    user.username   = update_user.username,
    user.phone      = update_user.phone,
    user.email      = update_user.email,
    user.adress     = update_user.adress,
    user.postalCode = update_user.postalCode,

    db.commit()

    return user

#* Route for deleted user
@router.delete(
    path="/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user by id",
    response_class=Response
)
def delete_user_by_id(user_id: str, db: Session = Depends(get_db), user: Log = Depends(get_current_user)):
    query = db.query(models.UserModel).filter(models.UserModel.id == user_id).delete()

    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    db.commit()