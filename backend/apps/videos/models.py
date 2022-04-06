from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database.database import Base

class VideoModel(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key = True)
    title = Column(String)
    content = Column(String)
    idUser = Column(String)
    idCategorie = Column(Integer)
    date = Column(DateTime)