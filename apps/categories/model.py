from sqlalchemy import Column,String, Integer
from database import base

class CategorieModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    labelCategorie = Column(String)
    descCategorie = Column(String)
    