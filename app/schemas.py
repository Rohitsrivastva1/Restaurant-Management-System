from pydantic import BaseModel,EmailStr

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
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(UserBase):
    password: str