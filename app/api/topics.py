from fastapi import APIRouter

from app.services.topic_service import (
    get_topics,
    topic_distribution
)

router = APIRouter()


@router.get("/topics")
def topics():

    return get_topics()


@router.get("/topic-distribution")
def distribution():

    return topic_distribution()