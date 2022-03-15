from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a token
@router.post("/token/", response_model=schemas.TokenSchema, status_code=status.HTTP_201_CREATED)
def create_token(token: schemas.TokenSchema, db: Session = Depends(get_db)):
    datas = models.tokenModel(
        id  = token.id,
        nbToken = token.nbToken,
        idOwnUser = token.idOwnUser
    )

    query = db.query(models.tokenModel).filter(token.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="token already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all token
@router.get("/token/get_all", response_model=List[schemas.TokenSchema])
def get_all_token(db: Session = Depends(get_db)):
    query = db.query(models.tokenModel).all()
    return query

# Create a get routes for get one token in the db.
@router.get("/token/{token_id}/", response_model=List[schemas.TokenSchema])
def get_all_token(token_id: str, db: Session = Depends(get_db)):
    query = db.query(models.tokenModel.id).filter(id == token_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] token doesn't exist")

    return query

# Route for update one token
@router.put("/token/update/{token_id}", response_model=schemas.TokenSchema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(token_id: str, update_token: schemas.TokenSchema, db: Session = Depends(get_db)):
    query = db.query(models.tokenModel).filter(update_token.id == token_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] token doesn't exist")

    update_data = models.tokenModel(
        labelCategorie = update_token.labelCategorie,
        descCategorie = update_token.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted token
@router.delete("token/{token_id}")
def delete_categorie_by_id(token_id: str, db: Session = Depends(get_db)):
    query : db.query(models.tokenModel).filter_by(id == token_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] token doesn't exist")
    else:
        db.delete()
        return "[204] No Content"