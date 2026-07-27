from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import APIs
from app.api.recommendation import router as recommendation_router
from app.api.student import router as student_router


app = FastAPI(
    title="Study Abroad Platform API"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
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