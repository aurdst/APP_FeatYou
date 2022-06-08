from datetime import datetime
from sqlalchemy import Float,Column,ForeignKey, Integer, String, DateTime
from database.database import Base

class EventModel(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key = True)
    label = Column(String)
    description = Column(String)
    idUser = Column(Integer)
    date = Column(String)
    price = Column(Float)
    sport = Column(String)
    adress = Column(String)
    duree = Column(String)
    hours = Column(String)
    listOfParticipant = Column(String)