from pydantic import BaseModel
from typing import Optional

from apps.users.schemas import UserSchema

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Log(UserSchema):
    session: str
    encrypted_pass: str