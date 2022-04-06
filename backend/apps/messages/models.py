from sqlalchemy import Float,Column,ForeignKey, Integer, String, DateTime
from database.database import Base

class MessageModel(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key = True)
    content = Column(String)
    idUser = Column(Integer)
    date = Column(DateTime)