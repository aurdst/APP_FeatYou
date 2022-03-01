from sqlalchemy import Float,Column,ForeignKey, Integer, String, DateTime
from database.database import Base

class ConversationModel(Base):
    __tablename__ = "conversation"

    id = Column(Integer, primary_key = True)
    idUsers = Column(String)
    idMessages = Column(String)