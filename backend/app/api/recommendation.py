from fastapi import APIRouter, HTTPException

from app.schemas.recommendation import RecommendationRequest
from app.services.recommendation_service import get_recommendations


router = APIRouter()


@router.post("/recommend")
def recommend(request: RecommendationRequest):

    try:
        result = get_recommendations(request)
        return result

    except Exception as e:
        print("FULL ERROR:", repr(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )