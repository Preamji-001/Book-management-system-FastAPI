from sqlalchemy import Column,Integer,String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from database import base

class Book(base):
    __tablename__= "books"
    id = Column(Integer,primary_key=True,nullable=False)
    title=Column(String,unique=True,nullable=False)
    author=Column(String,nullable=False)
    isbn=Column(Integer,unique=True,nullable=False)
    price=Column(Integer,nullable=False)
    quantity=Column(Integer,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
    
class User(base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    