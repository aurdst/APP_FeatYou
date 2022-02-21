from pydantic import BaseModel

class MessagesSchema(BaseModel):
    id: int
    content: str
    id_user: int