from fastapi import APIRouter

from app.services.trend_service import (
    get_topic_trends
)

router = APIRouter()


@router.get("/trends")
def trends():

    return get_topic_trends()