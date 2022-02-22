from datetime import datetime
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    firstName: str
    lastName: str
    role: str
    phone: str
    mail: str
    password: str
    postalCode: int
    banqCardNumber: int
    dateRegister: datetime
    adress: str

class UserViewSchema(BaseModel):
    firstName: str
    lastName: str
    role: int
    phone: str
    mail: str
    postalCode: int
    dateRegister: datetime