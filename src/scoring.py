# src/scoring.py

import pandas as pd

def compute_monthly_scores(df):
    score_map = {"Positive": 1, "Negative": -1, "Neutral": 0}
    df["score"] = df["sentiment"].map(score_map)

    # fix date parsing
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    df["month"] = df["date"].dt.to_period("M")

    # 'from' column = employee name
    monthly_scores = (
        df.groupby(["from", "month"])["score"]
        .sum()
        .reset_index()
    )

    return monthly_scores
