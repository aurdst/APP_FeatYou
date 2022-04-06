from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a subcategorie
@router.post("/subcategorie/", response_model=schemas.subcategories, status_code=status.HTTP_201_CREATED)
def create_subcategorie(subcategorie: schemas.subcategories, db: Session = Depends(get_db)):
    datas = models.subcategorieModel(
        id  = subcategorie.id,
        idCategorie = subcategorie.idCategorie,
        labelSubcategorie = subcategorie.labelSubcategorie,
        descSubcategorie = subcategorie.descSubcategorie
    )

    query = db.query(models.subcategorieModel).filter(subcategorie.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="subcategorie already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all subcategorie
@router.get("/subcategorie/get_all", response_model=List[schemas.subcategories])
def get_all_subcategorie(db: Session = Depends(get_db)):
    query = db.query(models.subcategorieModel).all()
    return query

# Create a get routes for get one subcategorie in the db.
@router.get("/subcategorie/{subcategorie_id}/", response_model=List[schemas.subcategories])
def get_all_subcategorie(subcategorie_id: str, db: Session = Depends(get_db)):
    query = db.query(models.subcategorieModel.id).filter(id == subcategorie_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] subcategorie doesn't exist")

    return query

# Route for update one subcategorie
@router.put("/subcategorie/update/{subcategorie_id}", response_model=schemas.subcategories, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(subcategorie_id: str, update_subcategorie: schemas.subcategories, db: Session = Depends(get_db)):
    query = db.query(models.subcategorieModel).filter(update_subcategorie.id == subcategorie_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Subcategorie doesn't exist")

    update_data = models.subcategorieModel(
        labelCategorie = update_subcategorie.labelCategorie,
        descCategorie = update_subcategorie.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted subcategorie
@router.delete("subcategorie/{subcategorie_id}")
def delete_categorie_by_id(subcategorie_id: str, db: Session = Depends(get_db)):
    query : db.query(models.subcategorieModel).filter_by(id == subcategorie_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Subcategorie doesn't exist")
    else:
        db.delete()
        return "[204] No Content"