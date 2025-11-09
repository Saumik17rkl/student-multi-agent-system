"""
Sentiment Analyzer Utility
--------------------------
Lightweight text sentiment classifier.
Used by Mental Health Agent for tone detection.
"""

from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """
    Analyzes sentiment polarity.
    Returns one of: 'positive', 'neutral', 'negative'
    """
    if not text:
        return "neutral"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"
