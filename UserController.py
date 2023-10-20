from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import models
from database import SessionLocal
from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_user(db: Session, user: UserBase):
    db = SessionLocal()
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(user_id: int):
    db = SessionLocal()
    return db.query(models.User).filter(models.User.id == user_id).first()

async def delete_user(db: Session, user_id: int):
    db_user = await db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )
    db.delete(db_user)
    db.commit()