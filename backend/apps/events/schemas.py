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
    lieu: str
    price: float
    sport: str

    class Config:
        orm_mode = True

class CreateEventSchema(BaseModel):
    label: str
    description: str
    date: str
    idUser: int 
    hours: str
    sport: str
    lieu: str
    price: float
    listOfParticipant : List[Participant] = []

    class Config:
        orm_mode = True