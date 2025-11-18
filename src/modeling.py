# src/modeling.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def build_regression_model(df):
    # Use 'body' as the text column
    df["msg_len"] = df["body"].astype(str).str.len()

    # Convert sentiment to numeric
    sentiment_map = {"Positive": 1, "Neutral": 0, "Negative": -1}
    df["sentiment_score"] = df["sentiment"].map(sentiment_map)

    # Basic feature: message length
    X = df[["msg_len"]]
    y = df["sentiment_score"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return {
        "model": model,
        "train_score": model.score(X_train, y_train),
        "test_score": model.score(X_test, y_test)
    }
