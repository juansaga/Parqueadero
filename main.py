import uvicorn
from fastapi import FastAPI

from app.router.parkin_router import router
from app.utils.db import Base, engine

app =FastAPI()

app.include_router(router=router)

Base.metadata.create_all(bind=engine)