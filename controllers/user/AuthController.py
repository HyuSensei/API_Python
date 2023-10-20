from fastapi import HTTPException, status
from database import SessionLocal
    
def registerUser(user):
    db= SessionLocal()
    if not user.email:
       raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng điền đủ thông tin !"
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
            "success": True,
            "message":"Đăng ký thành công !",
            "user": user
            }
    
    
    