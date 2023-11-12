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

@router.post("/api/v1/addProduct/",status_code=status.HTTP_201_CREATED)
async def addProducts(product: ProductsBase):
    try:
        data_product = models.Product(**product.dict())
        db_product  = AdminProductController.addProduct(data_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/prodouct/limit/{currentPage}",status_code=status.HTTP_201_CREATED)
async def getProduct(currentPage : int = Path(..., title="page", ge=1)):
    try:
        db_product  = AdminProductController.getProducts(currentPage)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/prodouct/count",status_code=status.HTTP_201_CREATED)
async def getCountProduct():
    try:
        db_product  = AdminProductController.countProducts()
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/product/{product_id}",status_code=status.HTTP_201_CREATED)
async def getProductsById(product_id: int = Path(..., title="ID sản phẩm cần lấy", ge=1)):
    try:
        db_product  = AdminProductController.getProductById(product_id)
        print(db_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/productByName/{product_name}",status_code=status.HTTP_201_CREATED)
async def getProductsByName(product_name: str = Path(..., title="nhap ten san pham")):
    try:
        db_product  = AdminProductController.getProductByName(product_name)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/productByNamePage/{product_name}/page/{currentPage}",status_code=status.HTTP_201_CREATED)
async def getProductsByNamePage(product_name: str, currentPage: int = Path(..., title="nhap ten san pham")):
    try:
        db_product  = AdminProductController.getProductByNamePage(product_name, currentPage)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.put("/api/v1/updateProduct/{product_id}",status_code=status.HTTP_201_CREATED)
async def updateProducts(product_id: int , product_data: ProductsBase):
    try:
        data_product = models.Product(**product_data.dict())
        db_product  = AdminProductController.updateProduct(product_id, data_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.delete("/api/v1/deleteProduct/{product_id}",status_code=status.HTTP_201_CREATED)
async def deleteProducts(product_id: int):
    try:
        db_product  = AdminProductController.deleteProduct(product_id)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )