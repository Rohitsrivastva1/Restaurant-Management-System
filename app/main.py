from fastapi import FastAPI
from .routers import manager, menu, orders
from .db import engine
from . import models
from app.auth.routes import router as auth_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(manager.router, prefix="/manager", tags=["manager"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
