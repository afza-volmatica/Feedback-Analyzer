import pandas as pd

from app.services.topic_classifier import (
    classify_topic
)


def get_topics():

    df = pd.read_csv(
        "data/amazon_reviews.csv",
        engine="python",
        on_bad_lines="skip"
    )

    results = []

    for _, row in df.iterrows():

        review = str(
            row["Review Text"]
        )

        topic = classify_topic(
            review
        )

        results.append(
            {
                "review": review[:100],
                "topic": topic
            }
        )

    return results


def topic_distribution():

    df = pd.read_csv(
        "data/amazon_reviews.csv",
        engine="python",
        on_bad_lines="skip"
    )

    counts = {}

    for _, row in df.iterrows():

        review = str(
            row["Review Text"]
        )

        topic = classify_topic(
            review
        )

        counts[topic] = (
            counts.get(topic, 0) + 1
        )

    return counts