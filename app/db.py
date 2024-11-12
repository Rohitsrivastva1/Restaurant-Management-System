# db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database URL (adjust this according to your database settings)
DATABASE_URL = "postgresql://rsadmin:fGA0SHmsnvbTNj4BbAIwZf2HKqUusPpS@dpg-cspn45e8ii6s73bq3jc0-a/qrcodedb_a0yh"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal class to create new session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
