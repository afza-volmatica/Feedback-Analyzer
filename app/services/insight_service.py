from app.services.topic_service import (
    topic_distribution
)


def get_insights():

    topics = topic_distribution()

    total_reviews = sum(
        topics.values()
    )

    top_topic = max(
        topics,
        key=topics.get
    )

    return {
        "total_reviews": total_reviews,
        "top_complaint": top_topic,
        "complaint_count": topics[top_topic]
    }