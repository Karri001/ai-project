# src/sentiment_labeler.py
from textblob import TextBlob
import pandas as pd

def get_sentiment(text):
    """Return Positive, Negative, or Neutral using TextBlob."""
    if pd.isna(text) or str(text).strip() == "":
        return "Neutral"

    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0.05:
        return "Positive"
    elif polarity < -0.05:
        return "Negative"
    else:
        return "Neutral"

def apply_sentiment(df):
    """Apply sentiment labeling using the 'body' column."""
    df["sentiment"] = df["body"].apply(get_sentiment)
    return df
