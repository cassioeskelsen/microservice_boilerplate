from fastapi import APIRouter
from typing import List

from cadastre.models.user import User

from cadastre.dispatch.cadastre_dispatch_service import send_user_to_broker

router = APIRouter()

@router.get("/",response_model=List[User])
def index():
    #TODO implement sample
    return []


@router.post("/")
def new_user(user: User):
    send_user_to_broker(user)
