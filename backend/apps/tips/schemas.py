from datetime import datetime
from pydantic import BaseModel
from pydantic.schema import Optional
# from typing import List

class TipsSchema(BaseModel):
    id: int
    content: str
    title: str
    category: str
    pict: Optional[str]


    class Config:
        orm_mode = True

class CreateTipsSchema(BaseModel):
    content: str
    title: str
    category: str
    pict: Optional[str]

    class Config:
        orm_mode = True

class UpdateTipsSchema(BaseModel):
    content: str
    title: str
    category: str
    pict: Optional[str]

    class Config:
        orm_mode = True