from fastapi import APIRouter, Depends, status, HTTPException, UploadFile
from sqlalchemy.orm import Session
from apps.auth.tools import get_current_user
from database.database import get_db
from typing import List
from apps.auth.tools import pwd_context
from passlib.context import CryptContext
from fastapi.responses import Response
from apps.auth.schemas import Log

from . import models
from . import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router: APIRouter = APIRouter()

#Route for create a user
@router.post(
    path="/create",
    # response_model=schemas.UserSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create new user"
)
def create_user(user: schemas.UserCreateSchema, file: UploadFile, db: Session = Depends(get_db)):
    datas = models.UserModel(
        firstName       = user.firstName,
        lastName        = user.lastName,
        username        = user.username,
        isadmin         = False,
        iscoach         = False,
        phone           = user.phone,
        email            = user.mail,
        hashed_password = pwd_context.hash(user.hashed_password),
        postalCode      = user.postalCode,
        banqCardNumb    = 0000000000000000,
        dateRegister    = user.dateRegister,
        adress          = user.adress,
        pict = file,
        lieux = user.lieux,
        sport = user.sport
    )

    query = db.query(models.UserModel).filter(models.UserModel.email == datas.email).first() 
    if query:
        raise HTTPException(status_code=409, detail="user already exist")
    
    db.add(datas)
    db.commit()
    db.refresh(datas)

    print(type(datas.file))

    return "201 Succes Account has been create"

#Create a get all user
@router.get(
    path="/get_all",
    response_model=List[schemas.UserViewSchema],
    summary="Get all user"
)
def get_all_user(db: Session = Depends(get_db), user: Log = Depends(get_current_user)):
    query = db.query(models.UserModel).all()
    return query

# Create a get routes for get one user in the db.
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

# Route for update one user
@router.put(
    path="/update/{user_id}",
    response_model=schemas.UpdateUserSchema,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update user by id"
)
def update_user(user_id: str, update_user: schemas.UpdateUserSchema, db: Session = Depends(get_db), user: Log = Depends(get_current_user)):

    item_to_update = db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
    if not item_to_update:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")
    else:
        item_to_update.firstName       = update_user.firstName,
        item_to_update.lastName        = update_user.lastName,
        item_to_update.username        = update_user.username,
        item_to_update.phone           = update_user.phone,
        item_to_update.email            = update_user.email,
        item_to_update.hashed_password = pwd_context.hash(update_user.hashed_password),
        item_to_update.postalCode      = update_user.postalCode,
        item_to_update.banqCardNumb    = update_user.banqCardNumb,
        item_to_update.adress          = update_user.adress,

        db.commit()

    return '202'

#Route for deleted user
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