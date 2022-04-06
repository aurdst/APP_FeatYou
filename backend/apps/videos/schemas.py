from datetime import datetime
from pydantic import BaseModel

class VideoSchema(BaseModel):
    id: int
    content: str
    title: str
    idUser: int
    idCategorie: int
    date: datetime

class VideoInsertSchema(BaseModel):
    content: str
    title: str
    idUser: int
    idCategorie: int
    date: datetime

    class Config:
        orm_mode = True