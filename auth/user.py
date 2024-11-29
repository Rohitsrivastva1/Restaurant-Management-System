from fastapi import APIRouter, Depends, HTTPException,Body, status
from sqlalchemy.orm import Session
from db import get_db
from Schemas.users import CreateUserSchema, UserSchema,UserLoginSchema
from sqlalchemy.orm import Session
from models import users as user_model
from services.db.user import create_user
from typing import Dict
from services.db import user as user_db_service

router = APIRouter()

@router.post('/signup',response_model=UserSchema)
def sign_up(session:Session=Depends(get_db),payload: CreateUserSchema=Body()):
    payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
    return create_user(session, user=payload)
    ...

@router.post('/login',response_model=Dict)
def login(payload:UserLoginSchema = Body(),session:Session=Depends(get_db)):

    print(payload)
    # return payload
    try:
        user:user_model.User = user_db_service.get_user_by_email(session, email=payload.email)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    is_validation:bool = user.validate_password(payload.password)

    if not is_validation:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    return {"access_tokekn":user.generate_token()}  