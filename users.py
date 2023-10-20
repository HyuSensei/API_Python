from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from controllers import UserController
from database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

class UserBase(BaseModel):
    username: str
    
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    try:
        db_user = UserController.create_user(db, user)
        return {"user": db_user}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int):
    db = SessionLocal()
    user = UserController.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not Found')
    return user


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserController.delete_user(db, user_id)
