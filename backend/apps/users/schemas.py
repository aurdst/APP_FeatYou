from datetime import datetime
from pydantic import BaseModel
from pydantic.schema import Optional
from typing import List

class UserSchema(BaseModel):
    id: int
    firstName: str
    lastName: str
    username: str
    isadmin: bool
    iscoach: bool
    phone: str
    email: str
    hashed_password: str
    postalCode: int
    banqCardNumb: int
    dateRegister: datetime
    adress: str
    pict: Optional[str]

    class Config:
        orm_mode = True


class Sport(BaseModel):
    sport: Optional[str]


class Lieu(BaseModel):
    sport: Optional[str]


class UpdateUserSchema(BaseModel):
    firstName: str
    lastName: str
    username: str
    phone: str
    email: str
    hashed_password: str
    postalCode: int
    banqCardNumb: int
    adress: str
    pict: Optional[str]
    sport: List[Sport] = []
    lieux: List[Lieu] = []

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    firstName: str
    lastName: str
    phone: str
    iscoach: bool
    adress: str
    mail: str
    postalCode: int
    dateRegister: datetime = datetime.utcnow()
    hashed_password: str
    pict: Optional[str]
    sport: Optional[str]
    lieux: Optional[str]

    class Config:
        orm_mode = True

class UserViewSchema(BaseModel):
    firstName: str
    lastName: str
    isadmin: Optional[bool]
    phone: str
    adress: str
    email: str
    postalCode: int
    banqCardNumb: int
    dateRegister: datetime = datetime.utcnow()
    pict: Optional[str]

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