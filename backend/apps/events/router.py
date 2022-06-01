from cProfile import label
from msilib import schema
from urllib import response
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a event
@router.post("/event/", response_model=schemas.EventSchema, status_code=status.HTTP_201_CREATED)
def create_event(event: schemas.EventSchema, db: Session = Depends(get_db)):
    datas = models.eventModel(
        id  = event.id,
        label = event.label,
        description = event.description,
        idCategorie = event.idCategorie,
        idUser = event.idUser,
        price = event.price,
        listOfParticipant = event.listOfParticipant
    )

    query = db.query(models.eventModel).filter(event.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="event already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all categorie
@router.get("/event/get_all", response_model=List[schemas.EventSchema])
def get_all_event(db: Session = Depends(get_db)):
    query = db.query(models.eventModel).all()
    return query

# Create a get routes for get one event in the db.
@router.get("/event/{event_id}/", response_model=List[schemas.EventSchema])
def get_all_event(event_id: str, db: Session = Depends(get_db)):
    query = db.query(models.eventModel.id).filter(id == event_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] event doesn't exist")

    return query

# Route for update one event
@router.put("/event/update/{event_id}", response_model=schemas.EventSchema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(event_id: str, update_event: schemas.EventSchema, db: Session = Depends(get_db)):
    query = db.query(models.eventModel).filter(update_event.id == event_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    update_data = models.eventModel(
        labelCategorie = update_event.labelCategorie,
        descCategorie = update_event.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted categorie
@router.delete("event/{event_id}")
def delete_categorie_by_id(event_id: str, db: Session = Depends(get_db)):
    query : db.query(models.eventModel).filter_by(id == event_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")
    else:
        db.delete()
        return "[204] No Content"