from fastapi import APIRouter, HTTPException, status, Path
from controllers.admin import AdminUserController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class UserBase(BaseModel):
    name : str
    email : str
    username : str
    password : str
    address : str
    role_id : int

@router.post("/addUser/",status_code=status.HTTP_201_CREATED)
async def addUser(user: UserBase):
    try:
        data_user = models.User(**user.dict())
        db_user  = AdminUserController.addUser(data_user)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/user/{user_id}",status_code=status.HTTP_201_CREATED)
async def getUsersById(user_id: int = Path(..., title="id người dùng", ge=1)):
    try:
        db_user  = AdminUserController.getUserById(user_id)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/userByUserName/{username}",status_code=status.HTTP_201_CREATED)
async def getUsersByUserName(username: str = Path(..., title="nhap ten nguoi dung")):
    try:
        db_user  = AdminUserController.getUserByUserName(username)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.put("/updateUser/{user_id}",status_code=status.HTTP_201_CREATED)
async def updateUsers(user_id: int , user_data: UserBase):
    try:
        data_user = models.User(**user_data.dict())
        db_user   = AdminUserController.updateUser(user_id, data_user)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.delete("/deleteUser/{user_id}",status_code=status.HTTP_201_CREATED)
async def deleteUsers(user_id: int):
    try:
        db_user  = AdminUserController.deleteUser(user_id)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )