from pydantic import BaseModel

class EventSchema(BaseModel):
    id: int
    label_event: str
    desc_event: str
    id_categorie: int
    id_user: int 
    cost_token: int