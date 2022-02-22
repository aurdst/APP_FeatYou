from pydantic import BaseModel

class EventSchema(BaseModel):
    id: int
    idUsers: list 
    idMessages: list