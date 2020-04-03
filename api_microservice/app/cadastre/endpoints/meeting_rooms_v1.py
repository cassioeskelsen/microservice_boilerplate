from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index():
    return {"Version": "1.0"}
