from pydantic import BaseModel,EmailStr

from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    isbn: int
    price:int
    quantity:int
    
class BookCreate(BookBase):
    pass

class BookFromServer(BookBase):
    id: int
    title:str
    author: str
    isbn: int
    price:int
    quantity:int
    created_at: datetime
    class Config:
        orm_mode=True
        
        
class UserCreate(BaseModel):
    email:EmailStr
    password:str
        
class UserProfileFromServer(BaseModel):
    id:int
    email:EmailStr
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
class Token(BaseModel):
    Access_Token: str
    Token_Type: str
    
class TokenData(BaseModel):
    email_address: EmailStr