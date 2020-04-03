from datetime import datetime

from pydantic import BaseModel

class Room(BaseModel):
    name: str

class Employeer(BaseModel):
    name: str

class RoomReservation(BaseModel):
    datehour: datetime
    room: Room
    employer: Employeer