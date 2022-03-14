from imp import reload
from typing import Optional
from fastapi import FastAPI, Response, Request
import uvicorn

from sqlalchemy import schema

from apps.categories.router import router as categories_router

app = FastAPI()

API_VERSION = "v1"

app.include_router(categories_router, tags=["Categories"], prefix=f"/api/{API_VERSION}/categories")


if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host= '127.0.0.1',
        port= 8000,
        reload= True
    )