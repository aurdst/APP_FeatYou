from sqlalchemy import Float,Column,ForeignKey, Integer, String, DateTime
from database.database import Base

class SubCategorieModel(Base):
    __tablename__ = "subcartegorie"

    id = Column(Integer, primary_key = True)
    labelSubcategorie = Column(String)
    descSubcategorie = Column(String)
    idCategorie = Column(Integer)