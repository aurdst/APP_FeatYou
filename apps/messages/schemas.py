from datetime import datetime
from pydantic import BaseModel

class MessagesSchema(BaseModel):
    id: int
    content: str
    idUser: int
    date: datetime