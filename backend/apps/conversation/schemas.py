from pydantic import BaseModel

class ConversationSchema(BaseModel):
    id: int
    idUsers: list 
    idMessages: list