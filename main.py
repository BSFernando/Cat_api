from fastapi import FastAPI
from model.schema import Base
from db.database import engine
import uvicorn
from routers import cat_router_del, cat_router_get, cat_router_post, cat_router_put
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logging.exception(logging.warning)

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(cat_router_get.router)
app.include_router(cat_router_post.router)
app.include_router(cat_router_put.router)
app.include_router(cat_router_del.router)

if __name__ == '__main__':
    uvicorn.run(app)
