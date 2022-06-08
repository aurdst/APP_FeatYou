from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from apps.users.schemas import CoachUserSchema

class Participant(BaseModel):
    id_participant: int

class EventSchema(BaseModel):
    id: int
    label: str
    description: str
    idUser: Optional[CoachUserSchema]
    date: str
    hours: str
    sport: str
    lieu: str
    price: float
    listOfParticipant : List[Participant] = []

    class Config:
        orm_mode = True

class AllEventSchema(BaseModel):
    id: int
    label: str
    description: str
    idUser: int
    date: str
    hours: str
    sport: str
    lieu: str
    price: float

    class Config:
        orm_mode = True

class CreateEventSchema(BaseModel):
    label: str
    description: str
    idUser: int 
    date: str
    hours: str
    sport: str
    lieu: str
    price: float

    class Config:
        orm_mode = True