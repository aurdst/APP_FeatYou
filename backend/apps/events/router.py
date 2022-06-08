import datetime
from datetime import timedelta
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List
from apps.users.router import get_coach
from apps.users.schemas import CoachUserSchema

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a event
@router.post("/create_event/", status_code=status.HTTP_201_CREATED)
def create_event(event: schemas.CreateEventSchema, db: Session = Depends(get_db)):
    datas = models.EventModel(
        label             = event.label,
        description       = event.description,
        date              = event.date,
        adress            = event.adress,
        idUser            = event.idUser,
        price             = event.price,
        hours             = event.hours,
        duree             = event.duree,
        sport             = event.sport,
        listOfParticipant = '[]'
    )

    query = db.query(models.EventModel).filter(models.EventModel.label == datas.label).first()
    if query:
        raise HTTPException(status_code=409, detail="event already exist")

    db.add(datas)
    db.commit()
    db.refresh(datas)
    
    return datas

#* Create a get all event
@router.get("/event/get_all")
def get_all_event(db: Session = Depends(get_db)):
    events = db.query(models.EventModel).all()

    for event in events :
        event.idUser = get_coach(event.idUser)

    return events

#* Get all event by sport
@router.get(
    "/events/{sport}",
    #response_model=List[schemas.EventSchema]
)
def get_by_sport(sport: str, db: Session = Depends(get_db)):
    events = db.query(models.EventModel).filter(models.EventModel.sport == sport.capitalize()).all()

    for event in events : 
        event.idUser = CoachUserSchema(**vars(get_coach(event.idUser, db)))

    return events

#* Create a get routes for get one event in the db.
@router.get("/event/{event_id}/", response_model=List[schemas.EventSchema])
def get_by_id(event_id: str, db: Session = Depends(get_db)):
    query = db.query(models.EventModel.id).filter(models.EventModel.id == event_id)

    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")

    return query

#* Route for update one event
@router.put("/event/update/{event_id}", response_model=schemas.EventSchema, status_code=status.HTTP_202_ACCEPTED)
def update_event(event_id: str, update_event: schemas.EventSchema, db: Session = Depends(get_db)):
    event = db.query(models.EventModel).filter(update_event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")

    event.label = update_event.label,
    event.description = update_event.description,

    db.commit()

    return event

#* Route for deleted event
@router.delete("event/{event_id}")
def delete_event_by_id(event_id: str, db: Session = Depends(get_db)):
    query : db.query(models.EventModel).filter_by(id == event_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")
    else:
        db.delete()
        return "[204] No Content"