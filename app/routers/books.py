from typing import Union,List
from fastapi import FastAPI , Response, status, HTTPException,Depends,APIRouter

from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from oauth2 import get_current_user


router= APIRouter(
    prefix="/book",
    tags=["Books"]
)


@router.get("/", response_model=List[schemas.BookFromServer])
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books  


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.BookFromServer)
def create_book(post: schemas.BookCreate,db:Session=Depends(get_db),current_user:str = Depends(get_current_user)):
    existing_book = db.query(models.Book).filter(models.Book.isbn == post.isbn).first()

    if existing_book:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book with this ISBN already exists")
    new_book=models.Book(**post.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book


@router.get("/{id}",response_model=schemas.BookBase)
def get_book(id:int,db:Session=Depends(get_db)):
    
    get_One_Book=db.query(models.Book).filter(models.Book.id == id).first()
    if not get_One_Book :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id:{id} was not found")
    
    return get_One_Book


@router.delete("/{id}")
def del_book(id:int,db:Session=Depends(get_db),current_user:str = Depends(get_current_user)):
    
    delete=db.query(models.Book).filter(models.Book.id==id)

    if delete.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id:{id} was not found")
    delete.delete(synchronize_session=False)
    db.commit()
    
    return "Booked Removed"


@router.put("/{id}",response_model=schemas.BookBase)
def update_book(id:int,books:schemas.BookBase,db:Session=Depends(get_db),current_user:str = Depends(get_current_user)):
    
    update=db.query(models.Book).filter(models.Book.id ==id).first()
    if update==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id:{id} was not found")
     # Update individual attributes of the update object
    for key, value in books.dict(exclude_unset=True).items():
        setattr(update, key, value)
    db.commit()
    db.refresh(update)
    
    return update