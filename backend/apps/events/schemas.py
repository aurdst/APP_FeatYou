from pydantic import BaseModel
from pydantic.schema import Optional
from typing import List

from apps.users.schemas import CoachUserSchema

class Participant(BaseModel):
    id_participant: int

class EventSchema(BaseModel):
    id: int
    label: str
    description: str
    idUser: CoachUserSchema 
    date: str
    hours: str
    adress: str
    duree: str
    price: float
    sport: str

    class Config:
        orm_mode = True

class AllEventSchema(BaseModel):
    id: int
    label: str
    description: str
    idUser: int
    date: str
    hours: str
    adress: str
    duree: str
    price: float
    sport: str

    class Config:
        orm_mode = True

class CreateEventSchema(BaseModel):
    label: str
    description: str
    idUser: int 
    date: str
    idUser: int 
    hours: str
    adress: str
    duree: str
    sport: str
    price: int
    listOfParticipant: List[Participant] = []

    class Config:
        orm_mode = True

class EventManaged(BaseModel):
    id_event:int
    id_participant:int
    ammount:int
    class Config:
        orm_mode = True