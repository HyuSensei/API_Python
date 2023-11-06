from fastapi import APIRouter, HTTPException, status,Path
from controllers.admin import AdminProductController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class ProductsBase(BaseModel):
    name: str
    image: str
    price: float
    description: str
    quantity: int
    category_id: int

@router.post("/addPoduct/",status_code=status.HTTP_201_CREATED)
async def addPoducts(product: ProductsBase):
    try:
        data_product = models.Product(**product.dict())
        db_product  = AdminProductController.addProduct(data_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/poduct/{product_id}",status_code=status.HTTP_201_CREATED)
async def getPoductsById(product_id: int = Path(..., title="ID sản phẩm cần lấy", ge=1)):
    try:
        db_product  = AdminProductController.getProductById(product_id)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/poductByName/{product_name}",status_code=status.HTTP_201_CREATED)
async def getPoductsById(product_name: str = Path(..., title="nhap ten san pham")):
    try:
        db_product  = AdminProductController.getProductByName(product_name)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.put("/updatePoduct/{product_id}",status_code=status.HTTP_201_CREATED)
async def updatePoducts(product_id: int , product_data: ProductsBase):
    try:
        data_product = models.Product(**product_data.dict())
        db_product  = AdminProductController.updateProduct(product_id, data_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.delete("/deletePoduct/{product_id}",status_code=status.HTTP_201_CREATED)
async def deletePoducts(product_id: int):
    try:
        db_product  = AdminProductController.deleteProduct(product_id)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )