from pydantic import BaseModel

class TokenSchema(BaseModel):
    id: int
    nbToken: str
    idOwnUser: int