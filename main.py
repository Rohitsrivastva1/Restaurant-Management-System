from fastapi import FastAPI,Depends,Body
from db import engine
from models import users as models
from auth import user as auth_router
from fastapi.middleware.cors import CORSMiddleware
from Schemas.users import CreateUserSchema, UserSchema
from sqlalchemy.orm import Session
from db import get_db
from models import users as user_model

from services.db.user import create_user

app = FastAPI()
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change to specific origins in production
    allow_credentials=True,  # Allows cookies to be included
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
# app.include_router(manager.router, prefix="/manager", tags=["manager"])
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])

