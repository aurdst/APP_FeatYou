from pydantic import BaseModel

class TokenSchema(BaseModel):
    id: int
    nb_token: str
    id_own_user: int