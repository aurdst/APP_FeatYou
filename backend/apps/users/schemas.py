from datetime import datetime
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    firstName: str
    lastName: str
    username: str
    role: str
    phone: str
    email: str
    password: str
    postalCode: int
    banqCardNumb: int
    dateRegister: datetime
    adress: str

    class Config:
        orm_mode = True

class UserViewSchema(BaseModel):
    firstName: str
    lastName: str
    role: int
    phone: str
    mail: str
    postalCode: int
    dateRegister: datetime

    class Config:
        orm_mode = True

class UserAuthSchema(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True

class UserInDB(UserAuthSchema):
    hashed_password: str

    class Config:
        orm_mode = True