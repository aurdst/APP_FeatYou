from msilib import schema
from urllib import response
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

@router.post("/conversation/", response_model=schemas.ConversationSchema, status_code=status.HTTP_201_CREATED)
def create_conversation(conversation: schemas.ConversationSchema, db: Session = Depends(get_db)):
    datas = models.ConversationModel(
        idMessages = conversation.idMessage,
        idUsers = conversation.idUsers
    )

    query = db.query(models.CategorieModel).filter(conversation.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="Conversation already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas