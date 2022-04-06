from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a user
@router.post("/user/", response_model=schemas.UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    datas = models.userModel(
        id = user.id,
        firstName = user.firstName,
        lastName = user.lastName,
        role = user.role,
        phone = user.phone,
        mail = user.mail,
        password = user.password,
        postalCode = user.postalCode,
        banqCardNumber = user.banqCardNumber,
        dateRegister = user.dateRegister,
        adress = user.adress
    )

    query = db.query(models.userModel).filter(user.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="user already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all user
@router.get("/user/get_all", response_model=List[schemas.UserViewSchema])
def get_all_user(db: Session = Depends(get_db)):
    query = db.query(models.userModel).all()
    return query

# Create a get routes for get one user in the db.
@router.get("/user/{user_id}/", response_model=List[schemas.UserViewSchema])
def get_all_user(user_id: str, db: Session = Depends(get_db)):
    query = db.query(models.userModel.id).filter(id == user_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    return query

# Route for update one user
@router.put("/user/update/{user_id}", response_model=schemas.UserSchema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(user_id: str, update_user: schemas.UserSchema, db: Session = Depends(get_db)):
    query = db.query(models.userModel).filter(update_user.id == user_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

    update_data = models.userModel(
        labelCategorie = update_user.labelCategorie,
        descCategorie = update_user.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted user
@router.delete("user/{user_id}")
def delete_categorie_by_id(user_id: str, db: Session = Depends(get_db)):
    query : db.query(models.userModel).filter_by(id == user_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")
    else:
        db.delete()
        return "[204] No Content"