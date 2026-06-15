from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retrieval_service import (
    search_reviews
)

router = APIRouter()


class SearchRequest(BaseModel):
    query: str


@router.post("/search")
def search(
    payload: SearchRequest
):

    results = search_reviews(
        payload.query
    )

    return {
        "query": payload.query,
        "results": results
    }