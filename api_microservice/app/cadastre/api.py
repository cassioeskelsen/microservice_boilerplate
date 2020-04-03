from fastapi import APIRouter
from cadastre.endpoints import users_v1
from cadastre.endpoints import meeting_rooms_v1

cadastre_api_router = APIRouter()
cadastre_api_router.include_router(users_v1.router, prefix="/v1/users", tags=["users"])
cadastre_api_router.include_router(meeting_rooms_v1.router, prefix="/v1/meeting_rooms", tags=["meeting_rooms"])
