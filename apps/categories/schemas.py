from pydantic import BaseModel

class CategoriesSchema(BaseModel):
    id: int
    labelCategorie: str
    descCategorie: str