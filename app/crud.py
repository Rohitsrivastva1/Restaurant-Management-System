from sqlalchemy.orm import Session
from . import models, schemas

def get_menu_items(db: Session):
    return db.query(models.MenuItem).all()

def create_menu_item(db: Session, item: schemas.MenuItemCreate):
    db_item = models.MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
