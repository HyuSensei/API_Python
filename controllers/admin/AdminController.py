from fastapi import HTTPException, status
from database import SessionLocal
from models import Order, Rate, Product, Category, OrderProduct
from sqlalchemy import func, extract
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from sqlalchemy.orm import joinedload

def getStatistics():
    try:
        
        db= SessionLocal()
        results = db.query(
            func.extract('month', Order.createdAt).label('month'),
            func.extract('year', Order.createdAt).label('year'),
            func.sum(Order.total).label('total_income')
        ).group_by('year', 'month').all()

        result_dict = {(result.year, result.month): result.total_income for result in results}

        # Get the start of the current year
        start_of_year = datetime(datetime.now().year, 1, 1)

        # Generate a list of months from the start of the year until now
        months = [(start_of_year + relativedelta(months=i)).month for i in range(12)]

        # Create a list of results with 0 for months without income
        final_results = [
            {"year": datetime.now().year, "month": month, "total_income": result_dict.get((datetime.now().year, month), 0)}
            for month in months
        ]

        return final_results
    except Exception as e:
        return {
            "success": False,
            "message": f"Error: {str(e)}"
        }
def getStatisticsByMonth():
    try:
        
        db= SessionLocal()
        start_of_month = datetime(datetime.now().year, datetime.now().month, 1)
        end_of_month = start_of_month + relativedelta(day=31)

        # Query to get total revenue for the current month
        total_revenue = db.query(func.sum(Order.total)).filter(Order.createdAt.between(start_of_month, end_of_month)).scalar()

        # Return the result
        return {"StatisticsByMonth": total_revenue or 0}
    except Exception as e:
        return {
            "success": False,
            "message": f"Error: {str(e)}"
        }
def getStatisticsByYear():
    try:
        
        db= SessionLocal()
        current_year = datetime.now().year

        # Thực hiện truy vấn để lấy doanh thu của năm hiện tại
        results = (
            db.query(func.sum(Order.total).label("total_revenue"))
            .filter(extract('year', Order.createdAt) == current_year)
            .first()
        )

        total_revenue = results.total_revenue if results.total_revenue is not None else 0

        return {"year": current_year, "total_revenue": total_revenue}
    except Exception as e:
        return {
            "success": False,
            "message": f"Error: {str(e)}"
        }
def getCuontRate():
    try:
        db = SessionLocal()
        countrate = db.query(func.count(Rate.id)).scalar()
        return {
            "success": True,
            "message": "thành công!",
            "countrate": countrate
        }
    except Exception as e:
        return {
            "success": False,
            "message": "thất bại!",
            "err": str(e)
        }
def getProductRate():
    try:
        db = SessionLocal()
        data = db.query(Rate).options(joinedload(Rate.product)).all()
        return {
            "success": True,
            "message": "thành công!",
            "data": data
        }
    except Exception as e:
        return {
            "success": False,
            "message": "thất bại!",
            "err": str(e)
        }
def getProductCategory():
    try:
        db = SessionLocal()
        categories = db.query(Category).all()
    
        category_data = []
        for category in categories:
            product_count = db.query(func.count(Product.id)).filter(Product.category_id == category.id).scalar()
            category_data.append({
                'category_name': category.name,
                'product_count': product_count
            })
        return {
            "success": True,
            "message": "thành công!",
            "product": category_data
        }
    except Exception as e:
        return {
            "success": False,
            "message": "thất bại!",
            "err": str(e)
        }
def getTopProductSale():
    try:
        db = SessionLocal()
        result = (
            db.query(Product, func.sum(OrderProduct.quantity))
            .join(OrderProduct, Product.id == OrderProduct.product_id)
            .group_by(Product.id)
            .order_by(func.sum(OrderProduct.quantity).desc())
            .all()
        )
        sold_products = [
            {"product_id": product.id, "product_name": product.name, "sold_quantity": sold_quantity}
            for product, sold_quantity in result
        ]
        return {
            "success": True,
            "message": "thành công!",
            "product": sold_products
        }
    except Exception as e:
        return {
            "success": False,
            "message": "thất bại!",
            "err": str(e)
        }