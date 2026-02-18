from fastapi import FastAPI

from api.routes import router
from api.websocket import ws_router
from config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name)
app.include_router(router)
app.include_router(ws_router)
