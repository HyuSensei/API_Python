from fastapi import APIRouter, HTTPException, status
from controllers.admin import AdminController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()


@router.get("/api/v1/getStatistics/",status_code=status.HTTP_200_OK)
async def getStatistics():
    try:
        data  = AdminController.getStatistics()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/getProductAdmin/",status_code=status.HTTP_200_OK)
async def getProductAdmin():
    try:
        data  = AdminController.getProductAdmin()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
        
@router.get("/api/v1/getStatisticsByMonth/",status_code=status.HTTP_200_OK)
async def getStatisticsByMonth():
    try:
        data  = AdminController.getStatisticsByMonth()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/getStatisticsByYear/",status_code=status.HTTP_200_OK)
async def getStatisticsByYear():
    try:
        data  = AdminController.getStatisticsByYear()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/countRate/",status_code=status.HTTP_200_OK)
async def countRate():
    try:
        data  = AdminController.getCuontRate()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/getProductRate/",status_code=status.HTTP_200_OK)
async def getProductRate():
    try:
        data  = AdminController.getProductRate()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/getProductCategory/",status_code=status.HTTP_200_OK)
async def getProductCategory():
    try:
        data  = AdminController.getProductCategory()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
        
@router.get("/api/v1/getTopProductSale/",status_code=status.HTTP_200_OK)
async def getTopProductSale():
    try:
        data  = AdminController.getTopProductSale()
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )