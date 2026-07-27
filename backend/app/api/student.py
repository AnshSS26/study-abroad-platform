from fastapi import APIRouter
from app.db.database import SessionLocal
from app.models.student import Student
from app.schemas.student import StudentCreate


router = APIRouter()


@router.post("/students")
def create_student(data: StudentCreate):

    db = SessionLocal()

    student = Student(
        **data.dict()
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    db.close()

    return student