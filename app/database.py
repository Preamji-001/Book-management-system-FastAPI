from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL='postgresql://preamji:0000@localhost/bms'
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

base = declarative_base()

#close db after yielding it 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()