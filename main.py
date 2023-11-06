from fastapi import  FastAPI
import models
from database import engine
from routes.user import auth
from routes.admin import categories, products , users, roles
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(roles.router)