import pandas as pd

from app.database.chroma_db import collection
from app.services.embedding_service import (
    generate_embedding
)


def load_reviews():

    if collection.count() > 0:
        print("Reviews already loaded.")
        return

    df = pd.read_csv(
        "data/Amazon_Reviews.csv",
        engine="python",
        on_bad_lines="skip"
    )

    # For testing only
    df = df.head(100)

    for idx, row in df.iterrows():

        review_text = str(
            row["Review Text"]
        )

        if review_text == "nan":
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
        f"Loaded {len(df)} reviews."
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