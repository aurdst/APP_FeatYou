from msilib import schema
from urllib import response
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()


#Route for create a conversation
@router.post("/conversation/", response_model=schemas.ConversationSchema, status_code=status.HTTP_201_CREATED)
def create_conversation(conversation: schemas.ConversationSchema, db: Session = Depends(get_db)):
    datas = models.ConversationModel(
        idMessages = conversation.idMessages,
        idUsers = conversation.idUsers
    )

    query = db.query(models.ConversationModel).filter(conversation.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="Conversation already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all categorie
@router.get("/conversation/get_all", response_model=List[schemas.ConversationSchema])
def get_all_conversation(db: Session = Depends(get_db)):
    query = db.query(models.ConversationModel).all()
    return query

# Create a get routes for get one conversation in the db.
@router.get("/conversation/{conversation_id}/", response_model=List[schemas.ConversationSchema])
def get_all_conversation(conversation_id: str, db: Session = Depends(get_db)):
    query = db.query(models.ConversationModel.id).filter(id == conversation_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Conversation doesn't exist")

    return query

# Route for update one conversation
@router.put("/conversation/update/{conversation_id}", response_model=schemas.ConversationSchema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(conversation_id: str, update_conversation: schemas.ConversationSchema, db: Session = Depends(get_db)):
    query = db.query(models.ConversationModel).filter(update_conversation.id == conversation_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    update_data = models.ConversationModel(
        labelCategorie = update_conversation.labelCategorie,
        descCategorie = update_conversation.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted categorie
@router.delete("conversation/{conversation_id}")
def delete_categorie_by_id(conversation_id: str, db: Session = Depends(get_db)):
    query : db.query(models.ConversationModel).filter_by(id == conversation_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")
    else:
        db.delete()
        return "[204] No Content"