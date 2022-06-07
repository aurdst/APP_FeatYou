from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from database.database import Base

class TipsModel(Base):
    __tablename__ = "tips"

    id = Column(Integer, primary_key = True)
    content = Column(String)
    title = Column(String)
    category = Column(String)
    pict = Column(String)