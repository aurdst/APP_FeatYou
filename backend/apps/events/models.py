from datetime import datetime
from sqlalchemy import Float,Column,ForeignKey, Integer, String, DateTime
from database.database import Base

class EventModel(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key = True)
    label = Column(String)
    description = Column(String)
    idCategorie = Column(Integer)
    idUser = Column(Integer)
    price = Column(Float)
    pict = Column(String)
    date = datetime.utcnow()