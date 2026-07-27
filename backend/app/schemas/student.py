from pydantic import BaseModel


class StudentCreate(BaseModel):

    name: str
    email: str

    preferred_country: str
    preferred_course: str

    budget: float
    currency: str

    cgpa: float
    ielts: float