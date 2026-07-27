from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    preferred_country: str
    preferred_course: str
    maximum_budget: float
    budget_currency: str
    cgpa: float
    ielts: float