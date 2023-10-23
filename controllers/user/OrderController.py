from fastapi import HTTPException, status
from database import SessionLocal
import models 
from sqlalchemy import func

def addOrder(data_order):
    db= SessionLocal()
    data_cart= data_order["cart"]
    if len(data_cart)==0:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail="Vui lòng thêm sản phẩm vào giỏ hàng !"
        )
    data_user= data_order["user"]
    if (not data_user["name"]) or (not data_user["address"]) or (not data_user["phone"]) or (not data_user["user_id"]):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail="Vui lòng điền đầy đủ thông tin đặt hàng !"
        )
    if (not data_user["method"]):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail="Vui lòng chọn phương thức thanh toán !"
        )
    if data_user["method"]=="ordervnpay":
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail="Hiện tại website SkinLeLe chưa hỗ trợ thanh toán VNPAY !"
        )
    total=0
    for i in range(len(data_cart)):
        total = data_cart[i]["price"] * data_cart[i]["quantity"]
    order_info = models.Order(
    payment="Thanh toán khi nhận hàng!",
    status=0,
    name=data_user["name"],
    address=data_user["address"],
    phone=data_user["phone"],
    total=total,
    user_id=data_user["user_id"]
    )
    db.add(order_info)
    db.commit()
    max_id_order = db.query(func.max(models.Order.id)).scalar()
    for i in range(len(data_cart)):
       order_product= models.OrderProduct(
           order_id= max_id_order,
           product_id= data_cart[i]["id"],
           quantity= data_cart[i]["quantity"]
       )
       db.add(order_product)
       db.commit()
    return {
        "success": True,
        "message": "Đặt hàng thành công !",
    }

def hanleOrderConfirm(user):
    db=SessionLocal()
    query = (
    db.query(models.Order, models.Product,models.OrderProduct)
    .join(models.OrderProduct, models.Order.id == models.OrderProduct.order_id)
    .join(models.Product, models.OrderProduct.product_id == models.Product.id)
    .filter(models.Order.user_id == user)
    )
    results = query.all()
    for order, product,order_product in results:
        print(order)
        print(product)
        print(order_product)
   


    