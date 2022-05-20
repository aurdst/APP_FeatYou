from fastapi import (
    APIRouter
)
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List
from dotenv import dotenv_values
import os

credentials = dotenv_values('')
# print(credentials)


class EmailSchema(BaseModel):
    email: List[EmailStr]

    class Config: 
        orm_mode = True

conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv("SMTP_EMAIL", "aureliendestailleur@outlook.fr"),
    MAIL_PASSWORD = os.getenv("SMTP_PASSWORD", """4851C2a172-mi"""),
    MAIL_FROM = "aureliendestailleur@outlook.fr",
    MAIL_PORT = 587,
    MAIL_SERVER = os.getenv("SMTP_HOST", "smtp.office365.com"),
    MAIL_FROM_NAME="FeatYou Team",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

router : APIRouter = APIRouter()


html = """
<p>Hi this test mail, thanks for using Fastapi-mail</p> 
"""


@router.post("/email")
async def simple_send(
    email: EmailSchema
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass 
        body=html,
        subtype="html"
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})