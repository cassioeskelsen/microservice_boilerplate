from fastapi import APIRouter
from api_v1.endpoints import home

api_router = APIRouter()
api_router.include_router(home.router, prefix="/v1", tags=["home"])
