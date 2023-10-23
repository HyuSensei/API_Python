from fastapi import APIRouter, HTTPException, status
from controllers.user import ProductController
from pydantic import BaseModel
import models

router=APIRouter()

class ProductBase(BaseModel):
    name: str
    image: str
    price: float
    description: str
    quantity: int
    category_id: int
    class Config:
        arbitrary_types_allowed = True

@router.get("/api/v1/products/home",status_code=status.HTTP_200_OK)
def getProductHome():
    try:
        data= ProductController.getProductHomeOne()
        print(data)
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.post("/api/v1/products/store",status_code=status.HTTP_201_CREATED)
def addProduct(product: ProductBase):
    try:
        data_product= models.Product(**product.dict())
        get_product= ProductController.storeProduct(data_product)
        return get_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )