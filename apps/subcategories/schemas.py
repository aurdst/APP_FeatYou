from pydantic import BaseModel

class subcategories(BaseModel):
    id: int
    labelSubcategorie: str
    descSubcategorie: str
    idCategorie: int