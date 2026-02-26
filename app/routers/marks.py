from fastapi import APIRouter, Depends
# هنا نستورد ملفات الجداول والاتصال التي تظهر عندك في مجلد models و dbs
# from app.models.marks import Mark 

router = APIRouter()

@router.get("/")
async def get_marks():
    # هنا الكود الذي يجلب البيانات من الـ Database
    return {"message": "قائمة العلامات من قاعدة البيانات"}

@router.post("/")
async def add_mark(mark_data: dict):
    # هنا الكود الذي يحفظ العلامة في قاعدة البيانات
    return {"status": "success", "message": "تم حفظ العلامة بنجاح"}