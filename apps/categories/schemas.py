from pydantic import BaseModel

class CategoriesSchema(BaseModel):
    id: int
    label_categorie: str
    desc_categorie: str