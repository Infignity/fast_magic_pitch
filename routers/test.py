"""lib import"""
from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def test_page():
    """test app working"""
    return {"Hello": "World"}
