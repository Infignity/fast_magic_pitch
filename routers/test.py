"""lib import"""
from fastapi import APIRouter
router = APIRouter()

@router.get("/test")
def test_page():
    """test app working"""
    return {"Hello": "World"}
