from Schemas.users import CreateUserSchema
from sqlalchemy.orm import Session
from models.users import User


def create_user(session:Session,user: CreateUserSchema):
  
    db_user = User(**user.dict())
  

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

    ...

def get_user_by_email(session:Session,email:str):
    return session.query(User).filter(User.email == email).one()

def get_user_by_id(session:Session,id:int):
    return session.query(User).filter(User.id == id).one()
