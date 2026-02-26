from fastapi import APIRouter, Depends
from ..models.major import Major

router = APIRouter()

@router.get("/")
async def get_majors():
    return {"message": "قائمة التخصصات"}

@router.post("/")
async def add_major(name: str):
    return {"status": "success", "major_name": name} 