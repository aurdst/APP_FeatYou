from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    firstName = Column(String)
    lastName = Column(String)   
    phone = Column(Integer)
    password = Column(String)
    adress = Column(String)
    dateRegister = Column(DateTime)
    email = Column(String)
    postalCode = Column(Integer)
    banqCardNumb = Column(Integer)
    role = Column(String)