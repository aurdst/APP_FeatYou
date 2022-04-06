from msilib import schema
from urllib import response
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Here we are a routes for Categories

# Create a post routes for create a categorie
@router.post("/categories/", response_model=schemas.CategoriesSchema, status_code=status.HTTP_201_CREATED)
def create_categorie(category: schemas.CategoriesSchema, db: Session = Depends(get_db)):
    new_datas = models.CategorieModel(
        labelCategorie = category.labelCategorie,
        descCategorie = category.descCategorie
    )

    query = db.query(models.CategorieModel).filter(models.CategorieModel.labelCategorie == new_datas.labelCategorie).first()
    if query:
        raise HTTPException(status_code=409, detail="[Conflict] : Categorie already exist")
    else:
        db.add(new_datas)
        db.commit()
        db.refresh(new_datas)
        
        return new_datas 

# Create a get routes for get all categories in the db.
@router.get("/categories/get_all", response_model=List[schemas.CategoriesSchema])
def get_all_categories(db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel).all()
    return query

# Create a get routes for get one categories in the db.
@router.get("/categories/{category_id}/", response_model=List[schemas.CategoriesSchema])
def get_all_categories(category_id: str, db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel.id).filter(id == category_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    return query

# Route for update one categories
@router.put("/categories/update/{category_id}", response_model=schemas.CategoriesSchema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(category_id: str, update_category: schemas.CategoriesSchema, db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel).filter_by(id == category_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    update_data = models.CategorieModel(
        labelCategorie = update_category.labelCategorie,
        descCategorie = update_category.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted categorie
@router.delete("categories/{category_id}")
def delete_categorie_by_id(category_id: str, db: Session = Depends(get_db)):
    query : db.query(models.CategorieModel).filter_by(id == category_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")
    else:
        db.delete()
        return "[204] No Content"