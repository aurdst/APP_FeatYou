from sqlalchemy import Float,Column,ForeignKey, Integer, String, DateTime
from database import Base

class TokenModel(Base):
    __tablename__ = "token"

    id = Column(Integer, primary_key = True)
    nbToken = Column(String)
    idOwnUser = Column(int)