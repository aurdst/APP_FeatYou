from pydantic import BaseModel

class CategoriesSchema(BaseModel):
    id: int
    labelCategorie: str
    descCategorie: str
    # url: str

    class Config:
        orm_mode = True

class UpdateCategorieSchema(BaseModel):
    labelCategorie: str
    descCategorie: str
    # url: str

    class Config:
        orm_mode = True