from datetime import datetime
from pydantic import BaseModel

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
    # pict: str

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

    class Config:
        orm_mode = True

class UserViewSchema(BaseModel):
    firstName: str
    lastName: str
    isadmin: bool
    phone: str
    mail: str
    postalCode: int
    dateRegister: datetime
    # pict: str

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