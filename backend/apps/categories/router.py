from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from sqlalchemy import insert
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List
import shutil
from .tools import id_generator
# import sqlalchemy_utils

from . import models
from apps.users import models
from . import schemas

#Auth with OAuth2
from fastapi.security import OAuth2PasswordBearer

router: APIRouter = APIRouter()

#Here we are a routes for Categories

# Create a post routes for create a categorie. //OK
@router.post(
    path="/add",
    status_code=status.HTTP_201_CREATED,
    summary="Add a categorie"
)
async def create_categorie(category: schemas.CategoriesSchema, db : Session = Depends(get_db)):

    create_datas = models.CategorieModel(
        labelCategorie = category.labelCategorie,
        descCategorie = category.descCategorie,
    )

    query = db.query(models.CategorieModel).filter(models.CategorieModel.labelCategorie == create_datas.labelCategorie).first()
    if query:
        raise HTTPException(status_code=409, detail="[Conflict] : Categorie already exist")
    else:
        db.add(create_datas)
        db.commit()
        db.refresh(create_datas)

    return create_datas

@router.post(
    path="/upload_file",
    status_code=status.HTTP_201_CREATED,
    summary="Add a file"
)
async def upload_file(user_id:int, file : UploadFile, db : Session = Depends(get_db)): #  url:str,
    # Error 422 : 422 Unprocessable Entity
    # When i try use file (param), the script return 422 Unprocessable Entity. I don't know why
    with open("uploaded/" + file.filename, "wb") as img:
        shutil.copyfileobj(file.file, img)

    url = str('uploaded/_'+id_generator()+file.filename)
    try:
        user = db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")

        print(type(user))

        # user.pict = url,

        # db.commit()

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
def get_categories(category_id: str, db: Session = Depends(get_db)):
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