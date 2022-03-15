from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a video
@router.post("/video/", response_model=schemas.Videochema, status_code=status.HTTP_201_CREATED)
def create_video(video: schemas.Videochema, db: Session = Depends(get_db)):
    datas = models.videoModel(
        id = video.id,
        firstName = video.firstName,
        lastName = video.lastName,
        role = video.role,
        phone = video.phone,
        mail = video.mail,
        password = video.password,
        postalCode = video.postalCode,
        banqCardNumber = video.banqCardNumber,
        dateRegister = video.dateRegister,
        adress = video.adress
    )

    query = db.query(models.videoModel).filter(video.id == datas.id).first()
    if query:
        raise HTTPException(status_code=404, detail="video already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all video
@router.get("/video/get_all", response_model=List[schemas.videoViewSchema])
def get_all_video(db: Session = Depends(get_db)):
    query = db.query(models.videoModel).all()
    return query

# Create a get routes for get one video in the db.
@router.get("/video/{video_id}/", response_model=List[schemas.videoViewSchema])
def get_all_video(video_id: str, db: Session = Depends(get_db)):
    query = db.query(models.videoModel.id).filter(id == video_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] video doesn't exist")

    return query

# Route for update one video
@router.put("/video/update/{video_id}", response_model=schemas.Videochema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(video_id: str, update_video: schemas.Videochema, db: Session = Depends(get_db)):
    query = db.query(models.videoModel).filter(update_video.id == video_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] video doesn't exist")

    update_data = models.videoModel(
        labelCategorie = update_video.labelCategorie,
        descCategorie = update_video.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted video
@router.delete("video/{video_id}")
def delete_categorie_by_id(video_id: str, db: Session = Depends(get_db)):
    query : db.query(models.videoModel).filter_by(id == video_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")
    else:
        db.delete()
        return "[204] No Content"