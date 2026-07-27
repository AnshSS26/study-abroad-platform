from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine

# Import models
from app.models.university import University
from app.models.program import Program
from app.models.admission_requirement import AdmissionRequirement
from app.models.student import Student

# Import APIs
from app.api.recommendation import router as recommendation_router
from app.api.student import router as student_router


# Create database tables
#Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Study Abroad Platform API"
)


# CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
app.include_router(recommendation_router)
app.include_router(student_router)



@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }