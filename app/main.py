from fastapi import FastAPI

from app.api.search import router as search_router
from app.api.topics import router as topic_router

from app.services.retrieval_service import load_reviews


app = FastAPI(
    title="AI Product Feedback Analyzer"
)

# Load reviews into ChromaDB at startup
load_reviews()

# Register routes
app.include_router(search_router)
app.include_router(topic_router)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

from app.api.trends import (
    router as trend_router
)

app.include_router(
    trend_router
)

from app.api.insights import (
    router as insight_router
)

app.include_router(
    insight_router
)