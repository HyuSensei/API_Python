from fastapi import HTTPException, status
from database import SessionLocal
import models

def getProductHomeOne():
    db=SessionLocal()
    get_product= db.query(models.Product).all()
    return {
        "success":True,
        "product":get_product
    }
    
def storeProduct(product):
    db=SessionLocal()
    db.add(product)
    db.commit()
    db.refresh(product)
    return {
        "success": True,
        "message": "Thêm sản phẩm thành công !",
        "product": product
    }

def handleProductDetail(product_id):
    db=SessionLocal()
    product= db.query(models.Product).filter(models.Product.id==product_id).first()
    return {
        "id":product.id,
        "name":product.name,
        "image":product.image,
        "price":product.price,
        "description":product.description,
        "category_id ":product.category_id
    }