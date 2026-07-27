from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String)

    preferred_country = Column(String)
    preferred_course = Column(String)

    budget = Column(Float)
    currency = Column(String)

    cgpa = Column(Float)
    ielts = Column(Float)