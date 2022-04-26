from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    firstName = Column(String)
    lastName = Column(String)
    username = Column(String)
    role = Column(String)
    phone = Column(String)
    email = Column(String)
    password = Column(String)
    postalCode = Column(Integer)
    banqCardNumb = Column(Integer)
    adress = Column(String)
    dateRegister = Column(DateTime)