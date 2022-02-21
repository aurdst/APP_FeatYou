from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    lastname: str
    role: int
    phone: str
    mail: str
    postal_code: int
    banq_card_number: int