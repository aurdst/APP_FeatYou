from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from apps.users.schemas import UserAuthSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return UserAuthSchema(
        firstName=token + "fakedecoded", mail="john@example.com", lastName="John Doe", role=1 
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user
