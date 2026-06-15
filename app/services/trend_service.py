import pandas as pd

from app.services.topic_classifier import (
    classify_topic
)


def get_topic_trends():

    df = pd.read_csv(
        "data/Amazon_Reviews.csv",
        engine="python",
        on_bad_lines="skip"
    )

    # Convert dates
    df["Review Date"] = pd.to_datetime(
        df["Review Date"],
        errors="coerce"
    )

    # Remove rows with invalid dates
    df = df.dropna(
        subset=["Review Date"]
    )

    # Create month column
    df["Month"] = (
        df["Review Date"]
        .dt.to_period("M")
        .astype(str)
    )

    trends = {}

    for _, row in df.iterrows():

        review = str(
            row["Review Text"]
        )

        topic = classify_topic(
            review
        )

        month = str(
            row["Month"]
        )

        key = (month, topic)

        trends[key] = (
            trends.get(key, 0) + 1
        )

    result = []

    for (month, topic), count in trends.items():

        result.append(
            {
                "month": month,
                "topic": topic,
                "count": int(count)
            }
        )

    return result