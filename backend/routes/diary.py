from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Diary
from database import get_db
from schemas import DiaryCreate
from datetime import date

# 创建路由
router = APIRouter()

@router.post("/diaries/")
def create_diary(diary: DiaryCreate, db: Session = Depends(get_db)):
    new_diary = Diary(
        user_id=diary.user_id,
        content=diary.content,
        visibility=diary.visibility,
        date=date.today()
    )
    db.add(new_diary)
    db.commit()
    db.refresh(new_diary)
    return {"detail": "Diary created successfully", "diary": new_diary}

@router.get("/diaries/{user_id}")
def get_diaries(user_id: int, db: Session = Depends(get_db)):
    diaries = db.query(Diary).filter(Diary.user_id == user_id).all()
    return {"diaries": diaries}