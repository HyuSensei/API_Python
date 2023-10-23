from fastapi import  FastAPI
import models
from database import engine
from routes.user import auth,web,order

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

app.include_router(web.router)

app.include_router(order.router)