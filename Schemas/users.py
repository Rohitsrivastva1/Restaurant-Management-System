from pydantic import BaseModel,Field


class UserBaseSchema(BaseModel):
    email:str
    full_name: str


class CreateUserSchema(UserBaseSchema):
    hashed_password: str = Field(alias="password")


class UserSchema(UserBaseSchema):
    id: int
    is_active: bool = Field(default=False)

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    email: str = Field(alias="username")
    password: str