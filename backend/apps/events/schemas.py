from pydantic import BaseModel

class EventSchema(BaseModel):
    id: int
    label: str
    description: str
    idCategorie: int
    idUser: int 
    price: float
    pict: str