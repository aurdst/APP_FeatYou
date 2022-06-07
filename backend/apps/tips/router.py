from unicodedata import category
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

router: APIRouter = APIRouter()

@router.post(
    path="/create",
    status_code=status.HTTP_201_CREATED,
    summary="Create new tips"
)
def create_tips(tips:schemas.CreateTipsSchema, db : Session = Depends(get_db)):
    new_tips_data = models.TipsModel(
        content = tips.content,
        title = tips.title,
        category = tips.category,
    )

    check_in_db = db.query(models.TipsModel).filter(models.TipsModel.title == new_tips_data.title).first()
    if check_in_db:
        raise HTTPException(status_code=409, detail="Tips already exist")
    
    db.add(new_tips_data)
    db.commit()
    db.refresh(new_tips_data)

    return new_tips_data

#* Create a get routes for get one user in the db.
@router.get(
    "/infos/{tips_id}", 
    response_model=schemas.TipsSchema,
    summary="Get tips by id"
)
def get_tips(tips_id: str, db: Session = Depends(get_db)):
    tips = db.query(models.TipsModel).filter(models.TipsModel.id == tips_id).first()
    if not tips:
        raise HTTPException(status_code=404, detail="[Not Found] Tips doesn't exist")

    return tips

#* Create a get routes for get one user in the db.
@router.get(
    "/allinfos", 
    response_model=List[schemas.TipsSchema],
    summary="Get all tips"
)
def get_all_tips( db: Session = Depends(get_db)):
    tips = db.query(models.TipsModel).all()
    if not tips:
        raise HTTPException(status_code=404, detail="[Not Found] Not tips in the db")

    return tips

#* Route for update one user
@router.put(
    path="/update/{tips_id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=schemas.TipsSchema,
    summary="Update tips by id"
)
def update_tips(tips_id: str, update_tips: schemas.UpdateTipsSchema, db: Session = Depends(get_db)):
    to_put = db.query(models.TipsModel).filter(models.TipsModel.id == tips_id).first()
    if not to_put:
        raise HTTPException(status_code=404, detail="[Not Found] Tips doesn't exist")

    to_put.content  = update_tips.content,
    to_put.title   = update_tips.title,
    to_put.category   = update_tips.category,
    to_put.pict      = update_tips.pict,

    db.commit()

    return to_put

#* Route for deleted user
@router.delete(
    path="/{tips_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete tips by id",
    response_class=Response
)
def delete_user_by_id(tips_id: str, db: Session = Depends(get_db), user: Log = Depends(get_current_user)):
    query = db.query(models.TipsModel).filter(models.TipsModel.id == tips_id).delete()

    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Tips doesn't exist")

    db.commit()