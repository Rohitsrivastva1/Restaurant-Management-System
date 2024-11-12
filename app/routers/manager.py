from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..db import get_db

router = APIRouter()

@router.post("/menu/items/", response_model=schemas.MenuItemOut)
def add_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return crud.create_menu_item(db=db, item=item)

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
