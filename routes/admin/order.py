from fastapi import APIRouter, HTTPException, status
from controllers.admin import AdminOrderController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()


@router.get("/api/v1/getAllOrder/",status_code=status.HTTP_200_OK)
async def getAllOrder():
    try:
        db_order  = AdminOrderController.getAllOrder()
        return db_order
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/getOrder/page/{currentPage}",status_code=status.HTTP_200_OK)
async def getOrderPage(currentPage: int):
    try:
        db_order  = AdminOrderController.getOrderPage(currentPage)
        return db_order
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.put("/api/v1/confirmOrder/{order_id}",status_code=status.HTTP_200_OK)
async def confirmOrder(order_id: int):
    try:
        db_order = AdminOrderController.confirmOrder(order_id)
        return db_order
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )    
@router.delete("/api/v1/deleteOrder/{order_id}",status_code=status.HTTP_200_OK)
async def deleteOrder(order_id: int):
    try:
        db_order = AdminOrderController.deleteOrder(order_id)
        return db_order
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
