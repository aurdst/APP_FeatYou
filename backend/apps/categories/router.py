from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List
import base64
import shutil

from . import models
from . import schemas

#Auth with OAuth2
from fastapi.security import OAuth2PasswordBearer

router: APIRouter = APIRouter()

#Here we are a routes for Categories

# Create a post routes for create a categorie. //OK
@router.post(
    path="/add",
    response_model=schemas.CategoriesSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Add a categorie"
)
async def create_categorie(category: schemas.CategoriesSchema,file : UploadFile, db : Session = Depends(get_db)):

    new_datas = models.CategorieModel(
        labelCategorie = category.labelCategorie,
        descCategorie = category.descCategorie,
    )

    query = db.query(models.CategorieModel).filter(models.CategorieModel.labelCategorie == new_datas.labelCategorie).first()
    if query:
        raise HTTPException(status_code=409, detail="[Conflict] : Categorie already exist")
    else:
        db.add(new_datas)
        db.commit()
        db.refresh(new_datas)
        
    return new_datas


@router.post(
    path="/uploadf_file",
    status_code=status.HTTP_201_CREATED,
    summary="Add a file"
)
async def upload_file(id:str, file : UploadFile, db : Session = Depends(get_db)): #  url:str,
    # Error 422 : 422 Unprocessable Entity
    # When i try use file (param), the script return 422 Unprocessable Entity. I don't know why 
    with open("uploaded/" + file.filename, "wb") as img:
        shutil.copyfileobj(file.file, img)

    url = str('uploaded/'+file.filename)
    try:
        query = db.query(models.CategorieModel).filter(models.CategorieModel.id == id).first()

        insert_img_into_db = models(
            
        )

        if not query:
            raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")
    except Exception as e:
        print(e)
        
    return file.content_type, url

# Create a get routes for get all categories in the db. //OK
@router.get(
    path = "/",
    response_model=List[schemas.CategoriesSchema],
    summary="Get all categorie"
)
def get_all_categories(db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel).all()
    return query

# Create a get routes for get one categories in the db. //OK
@router.get(
    path="/{category_id}",
    response_model=schemas.CategoriesSchema,
    summary="Get categorie by id"
)
def get_all_categories(category_id: str, db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel).filter(models.CategorieModel.id == category_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    return query

# Route for update one categories
@router.put(
    path="/{category_id}", 
    response_model=schemas.UpdateCategorieSchema, 
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update category"
)
def update_categorie(category_id: str, update_category: schemas.UpdateCategorieSchema, db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel).filter(models.CategorieModel.id == category_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    update_data = models.CategorieModel(
        labelCategorie = update_category.labelCategorie,
        descCategorie = update_category.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted categorie // OK
@router.delete(
    path="/{category_id}", 
    summary="Delete a category"
)
def delete_categorie_by_id(category_id: str, db: Session = Depends(get_db)):
    query = db.query(models.CategorieModel).filter(models.CategorieModel.id == category_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] Categorie doesn't exist")

    db.delete(query)
    db.commit()

    return "[204] No Content"