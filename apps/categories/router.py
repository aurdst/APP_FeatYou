from sqlalchemy import schema

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db

import crud
import model
import schemas

router: APIRouter = APIRouter()

#Here we are a routes for Categories

@router.post("/categories/", response_model=schemas.CategoriesSchema)
def createCategory(category: schemas.CategoriesSchema, db: Session = Depends(get_db)):
    return crud.createCategory(db=db, category=category)