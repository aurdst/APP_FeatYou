from imp import reload
from typing import Optional
from fastapi import FastAPI, Response, Request
import uvicorn

from sqlalchemy import schema

from apps.categories.router import router as categories_router
from apps.conversation.router import router as conversation_router
from apps.events.router import router as events_router
from apps.messages.router import router as messages_router
from apps.subcategories.router import router as subcategories_router
from apps.token.router import router as token_router
from apps.users.router import router as user_router
from apps.videos.router import router as video_router
from apps.auth.router import router as auth_router


app = FastAPI()

API_VERSION = "v1"

app.include_router(auth_router, tags=["Auth"], prefix=f"/api/{API_VERSION}/auth")
app.include_router(user_router, tags=["User"], prefix=f"/api/{API_VERSION}/user")
app.include_router(categories_router, tags=["Categories"], prefix=f"/api/{API_VERSION}/categories")
app.include_router(conversation_router, tags=["Conversation"], prefix=f"/api/{API_VERSION}/conversation")
app.include_router(events_router, tags=["Events"], prefix=f"/api/{API_VERSION}/events")
app.include_router(messages_router, tags=["Messages"], prefix=f"/api/{API_VERSION}/messages")
app.include_router(subcategories_router, tags=["SubCategories"], prefix=f"/api/{API_VERSION}/subcategories")
app.include_router(token_router, tags=["Coin"], prefix=f"/api/{API_VERSION}/coin")
app.include_router(video_router, tags=["Video"], prefix=f"/api/{API_VERSION}/video")


if __name__=="__main__":
    uvicorn.run(
        "main:app",
        host= '127.0.0.1',
        port= 8000,
        reload= True
    )