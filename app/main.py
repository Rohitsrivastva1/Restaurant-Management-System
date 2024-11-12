from fastapi import FastAPI
from .routers import manager, menu, orders
from .db import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(manager.router, prefix="/manager", tags=["manager"])
