from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

from . import models
from . import schemas

router: APIRouter = APIRouter()

#Route for create a video
@router.post("/", response_model=schemas.VideoInsertSchema, status_code=status.HTTP_201_CREATED)
def create_video(insert_video: schemas.VideoInsertSchema, db: Session = Depends(get_db)):
    datas = models.VideoModel(
        content = insert_video.content,
        title = insert_video.title,
        idUser = insert_video.idUser,
        idCategorie = insert_video.idCategorie,
        date = insert_video.date
    )

    query = db.query(models.VideoModel).filter(models.VideoModel.title == insert_video.title).first()
    if query:
        raise HTTPException(status_code=409, detail="video already exist")
    else:
        db.add(datas)
        db.commit()
        db.refresh(datas)
        
        return datas

#Create a get all video
@router.get("/video/get_all", response_model=List[schemas.VideoSchema])
def get_all_video(db: Session = Depends(get_db)):
    query = db.query(models.VideoModel).all()
    return query

# Create a get routes for get one video in the db.
@router.get("/video/{video_id}/", response_model=List[schemas.VideoSchema])
def get_all_video(video_id: str, db: Session = Depends(get_db)):
    query = db.query(models.VideoModel.id).filter(id == video_id)
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] video doesn't exist")

    return query

# Route for update one video
@router.put("/video/update/{video_id}", response_model=schemas.VideoSchema, status_code=status.HTTP_202_ACCEPTED)
def update_categorie(video_id: str, update_video: schemas.VideoSchema, db: Session = Depends(get_db)):
    query = db.query(models.VideoModel).filter(update_video.id == video_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] video doesn't exist")

    update_data = models.VideoModel(
        labelCategorie = update_video.labelCategorie,
        descCategorie = update_video.descCategorie,
    )

    db.commit()

    return update_data

#Route for deleted video
@router.delete("video/{video_id}")
def delete_categorie_by_id(video_id: str, db: Session = Depends(get_db)):
    query : db.query(models.VideoModel).filter_by(id == video_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="[Not Found] user doesn't exist")
    else:
        db.delete()
        return "[204] No Content"