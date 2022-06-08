from cProfile import label
from msilib import schema
from urllib import response
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List
from datetime import datetime

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a event
@router.post("/create_event/", status_code=status.HTTP_201_CREATED)
def create_event(event: schemas.CreateEventSchema, db: Session = Depends(get_db)):
    datas = models.EventModel(
        label = event.label,
        description = event.description,
        date = event.date,
        lieu = event.lieu,
        idUser = event.idUser,
        price = event.price,
        hours = event.hours,
        sport = event.sport
    )

    query = db.query(models.EventModel).filter(models.EventModel.label == datas.label).first()
    if query:
        raise HTTPException(status_code=409, detail="event already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all event
@router.get("/get_all", response_model=List[schemas.AllEventSchema])
def get_all_event(db: Session = Depends(get_db)):
    query = db.query(models.EventModel).all()
    return query

# Create a get routes for get one event in the db.
@router.get("/{event_id}/", response_model=schemas.EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    query = db.query(models.EventModel).filter(models.EventModel.id == event_id).all()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")

    return query

# Create a get routes for get one event in the db.
@router.get("/by_user/{user_id}/", response_model=List[schemas.AllEventSchema])
def get_by_user_id(user_id: int, db: Session = Depends(get_db)):
    query = db.query(models.EventModel).filter(models.EventModel.idUser == user_id).all()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")

    return query

# Route for update one event
@router.put("/update/{event_id}", response_model=schemas.EventSchema, status_code=status.HTTP_202_ACCEPTED)
def update_event(event_id: str, update_event: schemas.EventSchema, db: Session = Depends(get_db)):
    event = db.query(models.EventModel).filter(update_event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")

    event.label = update_event.label,
    event.description = update_event.description,


    db.commit()

    return event

#Route for deleted event
@router.delete("{event_id}")
def delete_event_by_id(event_id: str, db: Session = Depends(get_db)):
    query : db.query(models.EventModel).filter_by(id == event_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")
    else:
        db.delete()
        return "[204] No Content"