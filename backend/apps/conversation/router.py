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
@router.post(
    path="/add_conversation", 
    response_model=schemas.ConversationSchema, 
    status_code=status.HTTP_201_CREATED,
    summary="Add conversation"
    )
def create_conversation(conversation: schemas.ConversationSchema, db: Session = Depends(get_db)):
    datas = models.ConversationModel(
        idMessages = conversation.idMessages,
        idUsers = conversation.idUsers
    )

    query = db.query(models.ConversationModel).filter(models.ConversationModel.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="Conversation already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all categorie
@router.get(
    path="/conversation/", 
    response_model=List[schemas.ConversationSchema],
    summary="Get all conversation"
    )
def get_all_conversation(db: Session = Depends(get_db)):
    query = db.query(models.ConversationModel).all()
    return query

# Create a get routes for get one conversation in the db.
@router.get(
    path="/{conversation_id}",
    response_model=List[schemas.ConversationSchema],
    summary="Get conversation by id"
    )
def get_all_conversation(conversation_id: str, db: Session = Depends(get_db)):
    query = db.query(models.ConversationModel).filter(models.ConversationModel.id == conversation_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Conversation doesn't exist")

    return query

# Route for update one conversation
@router.put(
    path="/{conversation_id}", 
    response_model=schemas.ConversationSchema, 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update Conversation"
    )
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
@router.delete(
    path="/{conversation_id}",
    summary="Delete a conversation"
    )
def delete_categorie_by_id(conversation_id: str, db: Session = Depends(get_db)):
    query : db.query(models.ConversationModel).filter_by(id == conversation_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")
    else:
        db.delete()
        return "[204] No Content"