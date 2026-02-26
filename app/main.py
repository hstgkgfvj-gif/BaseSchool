from fastapi import FastAPI
from .routers import marks, students, majors, subjects

app = FastAPI()

app.include_router(marks.router, prefix="/marks", tags=["Marks"])
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(majors.router, prefix="/majors", tags=["Majors"])
app.include_router(subjects.router, prefix="/subjects", tags=["Subjects"])

@app.get("/")
async def root():
    return {"message": "BaseSchool API is running"}