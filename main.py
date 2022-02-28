from imp import reload
from typing import Optional
from fastapi import FastAPI
import uvicorn

from sqlalchemy import schema

from apps.categories.router import router as avai_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host= '127.0.0.1',
        port= 8000,
        reload= True
    )