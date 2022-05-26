from pydantic import BaseModel

class CategoriesSchema(BaseModel):
    labelCategorie: str
    descCategorie: str

    class Config:
        orm_mode = True

class UpdateCategorieSchema(BaseModel):
    labelCategorie: str
    descCategorie: str

    class Config:
        orm_mode = True