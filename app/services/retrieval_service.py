import pandas as pd
from pathlib import Path

from app.database.chroma_db import collection
from app.services.embedding_service import (
    generate_embedding
)

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# CSV Path
CSV_PATH = BASE_DIR / "data" / "Amazon_Reviews.csv"


def load_reviews():

    # Don't reload if already populated
    if collection.count() > 0:
        print("Reviews already loaded.")
        return

    # Check file exists
    if not CSV_PATH.exists():
        print(f"CSV file not found: {CSV_PATH}")
        return

    df = pd.read_csv(
        CSV_PATH,
        engine="python",
        on_bad_lines="skip"
    )

    # Optional: limit for testing
    df = df.head(100)

    for idx, row in df.iterrows():

        review_text = str(
            row.get("Review Text", "")
        )

        if (
            review_text == "nan"
            or review_text.strip() == ""
        ):
            continue

        collection.add(
            ids=[str(idx)],
            documents=[review_text],
            embeddings=[
                generate_embedding(
                    review_text
                )
            ]
        )

    print(
        f"Loaded {collection.count()} reviews."
    )


def search_reviews(
    query: str,
    top_k: int = 5
):

    query_embedding = generate_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    return results["documents"][0]