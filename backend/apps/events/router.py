import datetime
from datetime import timedelta
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List
from apps.users.router import get_coach, manage_coin
from apps.users.schemas import CoachUserSchema, UserCoinSchema

from . import models
from . import schemas

router: APIRouter = APIRouter()

#* Route for create a event
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

#* Get all event
@router.get("/event/get_all", response_model=List[schemas.AllEventSchema])
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
@router.get("/event/{event_id}/", response_model=schemas.EventSchema)
def get_by_id(event_id: int, db: Session = Depends(get_db)):
    query = db.query(models.EventModel).filter(models.EventModel.id == event_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")

    return query

#* Create a get routes for get one event in the db by user id.
@router.get(
    "/by_user/{user_id}/", 
)
def get_by_user_id(user_id: int, db: Session = Depends(get_db)):
    events = db.query(models.EventModel).all()
    e      = []

    for event in events:
        if not event.listOfParticipant :
            continue

        id_participants = list(event.listOfParticipant[1:-1].split(","))

        if id_participants.count(user_id) == 0 :
            e.append(event)

    query = db.query(models.EventModel).filter(models.EventModel.idUser == user_id).all()

    if not query and len(e) == 0:
        raise HTTPException(status_code=404, detail="[404 NOT FOUND] You aren't foud in any event's participants")

    return [e, query]

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
    query = db.query(models.EventModel).filter_by(id == event_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")
    else:
        db.delete()
        return "[204] No Content"

#* Route for manage participants of a event by using event.id
@router.put("/manage_paricipant", status_code=status.HTTP_202_ACCEPTED)
def manage_participant(event_managed:schemas.EventManaged, db: Session = Depends(get_db)) :
    event = get_by_id(event_managed.id_participant, db)
    event_managed.id_participant = str(event_managed.id_participant)

    #* Parse '[ ]' return in db by valid python's List object
    id_participants = list(event.listOfParticipant[1:-1].split(","))

    if id_participants.count(event_managed.id_participant) > 0 :
        raise HTTPException(status_code=409, detail="[ERROR 409 - Conflits in participant] You already participate at this event")

    id_participants.append(event_managed.id_participant)
    event.listOfParticipant = '[' + ','.join([str(item) for item in id_participants]) + ']'

    userCoinData = {
        "id"      : event_managed.id_participant,
        "ammount" : event_managed.ammount,
        "operator": '-'
    }

    manage_coin(UserCoinSchema(**userCoinData), db)

    db.commit()

    return event