from datetime import datetime
from pydantic import BaseModel

class Videochema(BaseModel):
    id: int
    content: str
    title: str
    idUser: int
    idcategorie: int
    date: datetime