from fastapi import FastAPI
from .routers import manager, menu, orders
from .db import engine
from . import models
from app.auth.routes import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change to specific origins in production
    allow_credentials=True,  # Allows cookies to be included
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
app.include_router(manager.router, prefix="/manager", tags=["manager"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
