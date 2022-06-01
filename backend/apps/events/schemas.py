from pydantic import BaseModel
from typing import List

class Participant(BaseModel):
    id_participant: int
class EventSchema(BaseModel):
    id: int
    label: str
    description: str
    idCategorie: int
    idUser: int 
    price: float
    pict: str
    listOfParticipant : List[Participant] = []