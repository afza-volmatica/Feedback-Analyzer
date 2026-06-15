import streamlit as st
import requests
import pandas as pd

# ----------------------------------
# CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Product Feedback Analyzer",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# ----------------------------------
# API FUNCTIONS
# ----------------------------------

def get_insights():
    try:
        response = requests.get(
            f"{API_URL}/insights"
        )
        return response.json()
    except:
        return None


def get_distribution():
    try:
        response = requests.get(
            f"{API_URL}/topic-distribution"
        )
        return response.json()
    except:
        return None


def get_trends():
    try:
        response = requests.get(
            f"{API_URL}/trends"
        )
        return response.json()
    except:
        return []


def search_reviews(query):

    try:
        response = requests.post(
            f"{API_URL}/search",
            json={
                "query": query
            }
        )

        return response.json()

    except Exception as e:
        return {
            "error": str(e)
        }


# ----------------------------------
# TITLE
# ----------------------------------

st.title(
    "📊 AI Product Feedback Analyzer"
)

st.markdown(
    """
Analyze customer feedback, complaints,
topics, trends, and semantic search results.
"""
)

# ----------------------------------
# INSIGHTS SECTION
# ----------------------------------

st.header("📈 Business Insights")

insights = get_insights()

if insights:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Reviews",
            insights.get(
                "total_reviews",
                0
            )
        )

    with col2:
        st.metric(
            "Top Complaint",
            insights.get(
                "top_complaint",
                "N/A"
            )
        )

    with col3:
        st.metric(
            "Complaint Count",
            insights.get(
                "complaint_count",
                0
            )
        )

else:
    st.warning(
        "Could not fetch insights."
    )

st.divider()

# ----------------------------------
# TOPIC DISTRIBUTION
# ----------------------------------

st.header("📊 Complaint Distribution")

distribution = get_distribution()

if distribution:

    df_dist = pd.DataFrame(
        distribution.items(),
        columns=[
            "Topic",
            "Count"
        ]
    )

    st.bar_chart(
        df_dist.set_index(
            "Topic"
        )
    )

    st.dataframe(
        df_dist,
        use_container_width=True
    )

else:
    st.warning(
        "No topic distribution data found."
    )

st.divider()

# ----------------------------------
# TRENDS
# ----------------------------------

st.header("📈 Complaint Trends")

trends = get_trends()

if len(trends) > 0:

    df_trends = pd.DataFrame(
        trends
    )

    pivot_df = df_trends.pivot_table(
        index="month",
        columns="topic",
        values="count",
        fill_value=0
    )

    st.line_chart(
        pivot_df
    )

    st.dataframe(
        df_trends,
        use_container_width=True
    )

else:
    st.warning(
        "No trend data found."
    )

st.divider()

# ----------------------------------
# SEMANTIC SEARCH
# ----------------------------------

st.header("🔍 Semantic Review Search")

query = st.text_input(
    "Search customer reviews",
    placeholder="refund issue"
)

if st.button(
    "Search"
):

    if query.strip() == "":
        st.warning(
            "Please enter a query."
        )

    else:

        results = search_reviews(
            query
        )

        st.subheader(
            "Results"
        )

        st.json(
            results
        )

st.divider()

# ----------------------------------
# TOPICS
# ----------------------------------

st.header("🏷️ Classified Topics")

try:

    response = requests.get(
        f"{API_URL}/topics"
    )

    topics = response.json()

    df_topics = pd.DataFrame(
        topics
    )

    st.dataframe(
        df_topics,
        use_container_width=True
    )

except:
    st.warning(
        "Could not load topics."
    )

# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()

st.caption(
    "AI Product Feedback Analyzer | FastAPI + ChromaDB + Streamlit"
)