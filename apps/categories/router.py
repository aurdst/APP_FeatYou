from urllib import response
from sqlalchemy import schema

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Here we are a routes for Categories

# Create a post routes for create à categorie
@router.post("/categories/", response_model=schemas.CategoriesSchema)
def createCategory(category: schemas.CategoriesSchema, db: Session = Depends(get_db)):
    db.query(models.CategorieModel).filter_by(models.CategorieModel.labelCategorie).first()
    if models.CategorieModel.labelCategorie == category.labelCategorie:
        raise HTTPException(status_code=404, details="Categorie already exist")
    else:
        insert_data_in_db = models.CategorieModel(
            labelCategorie = category.labelCategorie,
            descCategorie = category.descCategorie
        )
        db.add(insert_data_in_db)
        db.commit()
        db.refresh(insert_data_in_db)
        
        return insert_data_in_db 

# Create a get routes for get all categories in the db.
@router.get("/categories/get_all", response_model=List[schemas.CategoriesSchema])
def getAllCategories(db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel).all()
    return query
