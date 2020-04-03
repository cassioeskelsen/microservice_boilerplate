from fastapi import APIRouter
from reservations.endpoints import reservations_v1


reservations_api_router = APIRouter()
reservations_api_router.include_router(reservations_v1.router, prefix="/v1/reservations", tags=["reservations"])

