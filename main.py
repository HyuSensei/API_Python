from fastapi import  FastAPI
import models
from database import engine
from routes.user import auth
from routes.admin import categories as admincategories, products , users, roles,  authadmin, order as adminOrder, admin
from routes.user import auth,web,order,rating,categories

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(adminOrder.router)


app.include_router(roles.router)

app.include_router(web.router)

app.include_router(order.router)

app.include_router(rating.router)

app.include_router(admincategories.router)

app.include_router(authadmin.router)