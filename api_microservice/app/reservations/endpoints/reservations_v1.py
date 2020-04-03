from fastapi import APIRouter

from reservations.models.room_reservation import RoomReservation

router = APIRouter()

@router.get("/")
def index():
    return {"Version": "1.0"}

@router.post("/")
def index(room_reservation: RoomReservation):
    pass
