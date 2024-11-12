from pydantic import BaseModel

class MenuItemCreate(BaseModel):
    section_id: int
    name: str
    description: str
    price: float
    is_active: bool = True

class MenuItemOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True
