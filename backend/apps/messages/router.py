from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a message
@router.post("/message/", response_model=schemas.MessagesSchema, status_code=status.HTTP_201_CREATED)
def create_message(message: schemas.MessagesSchema, db: Session = Depends(get_db)):
    datas = models.MessageModel(
        id  = message.id,
        content = message.label,
        description = message.description,
        idCategorie = message.idCategorie,
        idUser = message.idUser,
        price = message.price
    )

    query = db.query(models.MessageModel).filter(message.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="message already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all categorie
@router.get("/message/get_all", response_model=List[schemas.MessagesSchema])
def get_all_message(db: Session = Depends(get_db)):
    query = db.query(models.MessageModel).all()
    return query

# Create a get routes for get one message in the db.
@router.get("/message/{message_id}/", response_model=List[schemas.MessagesSchema])
def get_all_message(message_id: str, db: Session = Depends(get_db)):
    query = db.query(models.MessageModel.id).filter(id == message_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] message doesn't exist")

    return query

# Route for update one message
@router.put("/message/update/{message_id}", response_model=schemas.MessagesSchema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(message_id: str, update_message: schemas.MessagesSchema, db: Session = Depends(get_db)):
    query = db.query(models.MessageModel).filter(update_message.id == message_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    update_data = models.MessageModel(
        labelCategorie = update_message.labelCategorie,
        descCategorie = update_message.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted categorie
@router.delete("message/{message_id}")
def delete_categorie_by_id(message_id: str, db: Session = Depends(get_db)):
    query : db.query(models.MessageModel).filter_by(id == message_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")
    else:
        db.delete()
        return "[204] No Content"