from sqlalchemy import schema

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Here we are a routes for Categories

@router.post("/categories/", response_model=schemas.CategoriesSchema)
def createCategory(category: schemas.CategoriesSchema, db: Session = Depends(get_db)):
    insert_data_in_db = models.CategorieModel(
        labelCategorie = category.labelCategorie,
        descCategorie = category.descCategorie
    )
    db.add(insert_data_in_db)
    db.commit()
    db.refresh(insert_data_in_db)
    
    return insert_data_in_db 
