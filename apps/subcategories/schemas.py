from pydantic import BaseModel

class subcategories(BaseModel):
    id: int
    label_subcategorie: str
    desc_subcategorie: str
    id_categorie: int