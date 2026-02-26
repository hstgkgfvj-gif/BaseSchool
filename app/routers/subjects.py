from fastapi import APIRouter, Depends
from ..models.subject import Subject

router = APIRouter()

@router.get("/")
async def get_subjects():
    return {"message": "قائمة المواد الدراسية"}

@router.post("/")
async def add_subject(name: str, major_id: int):
    return {"status": "success", "subject_name": name, "major_id": major_id}