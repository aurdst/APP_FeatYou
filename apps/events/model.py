from sqlalchemy import Float,Column,ForeignKey, Integer, String, DateTime
from database import Base

class EventModel(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key = True)
    label = Column(String)
    description = Column(String)
    idCategorie = Column(int)
    idUser = Column(int)
    price = Column(Float)