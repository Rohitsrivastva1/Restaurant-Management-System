from fastapi import APIRouter, Depends, HTTPException,Body, status
from sqlalchemy.orm import Session
from db import get_db
from Schemas.users import CreateUserSchema, UserSchema,UserLoginSchema
from sqlalchemy.orm import Session
from models import users as user_model
from services.db.user import create_user
from typing import Dict
from services.db import user as user_db_service
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
router = APIRouter()

@router.get("/analytics/")
def get_sales_data(db: Session = Depends(get_db)):
    # Sample data structure for analytics
    sample_data = {
        "total_sales": 45000,
        "total_orders": 120,
        "top_selling_items": [
            {"item_name": "Pasta", "sales": 12000, "orders": 30},
            {"item_name": "Chinese Platter", "sales": 8000, "orders": 20},
            {"item_name": "Pizza", "sales": 5000, "orders": 15}
        ],
        "sales_by_category": {
            "Italian": {"sales": 20000, "orders": 50},
            "Chinese": {"sales": 15000, "orders": 40},
            "Desserts": {"sales": 10000, "orders": 30}
        },
        "daily_sales": [
            {"date": "2024-11-01", "sales": 7000},
            {"date": "2024-11-02", "sales": 8000},
            {"date": "2024-11-03", "sales": 6000},
            {"date": "2024-11-04", "sales": 9000},
            {"date": "2024-11-05", "sales": 7000}
        ]
    }
    return sample_data