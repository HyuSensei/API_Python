from fastapi import APIRouter, HTTPException, status
from controllers.user import AuthController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class UserBase(BaseModel):
    name: str
    email: str
    username: str
    password: str
    address: str
    role_id: int

@router.post("/register/",status_code=status.HTTP_201_CREATED)
async def registerUser(user: UserBase):
    try:
        data_user = models.User(**user.dict())
        db_user = AuthController.registerUser(data_user)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )