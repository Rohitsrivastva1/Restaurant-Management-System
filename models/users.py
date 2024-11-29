from sqlalchemy import Column, Integer, String, Boolean, LargeBinary,UniqueConstraint,PrimaryKeyConstraint
from db import Base
import bcrypt

import jwt

SECRET = "supersecretkey1"

class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True, nullable=False)
    full_name = Column(String(225), nullable=False)
    email = Column(String(225), unique=True,  nullable=False)
    hashed_password = Column(LargeBinary, nullable=False)
    is_active = Column(Boolean, default=False)

    UniqueConstraint('email', name='uq_user_email')
    PrimaryKeyConstraint('id', name='pk_user_id')

    def __repr__(self):
        return f"<User {full_name!r}>.format(full_name=self.full_name)"
    
    @staticmethod
    def hash_password(password: str) -> str:

        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def validate_password(self, password: str) -> bool:
        if bcrypt.checkpw(password.encode(), self.hashed_password):

            return{
                "access_token": jwt.encode(
                    {"full_name": self.full_name, "email":self.email}, SECRET)
            }
        
        else:
            return False
        
    def generate_token(self) -> dict:
        return {
            "access_token": jwt.encode(
                {"full_name": self.full_name, "email":self.email}, SECRET)
        }
        
def get_profile():

    # user_id_from_token = decode_token(token)
    # print(user_id_from_token)

    return user_db_service.get_user_by_id(session=session, id=id)
    