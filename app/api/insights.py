from fastapi import APIRouter

from app.services.insight_service import (
    get_insights
)

router = APIRouter()


@router.get("/insights")
def insights():

    return get_insights()