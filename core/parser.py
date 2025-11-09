"""
Input Parser
-------------
Cleans and normalizes incoming text, removes noise,
detects basic entities (like subjects, dates, and emotion clues),
and standardizes the format for intent routing.
"""

import re
import datetime
from utils.sentiment_analyzer import analyze_sentiment


def clean_text(text: str) -> str:
    """Normalize text: lowercase, remove excessive whitespace and special chars."""
    text = text.strip().lower()
    # Replace newlines, tabs, etc.
    text = re.sub(r"\s+", " ", text)
    # Remove emojis and non-alphanumeric except essential punctuation
    text = re.sub(r"[^a-z0-9\s\.\,\?\!]", "", text)
    return text


def extract_entities(text: str) -> dict:
    """Extract lightweight entities from text using regex and keyword cues."""
    entities = {}

    # Detect academic keywords
    if any(word in text for word in ["exam", "assignment", "lecture", "course", "subject", "topic"]):
        entities["domain"] = "academic"

    # Finance/admin cues
    if any(word in text for word in ["budget", "fee", "scholarship", "register", "form", "payment"]):
        entities["domain"] = "finance"

    # Extract date-like patterns
    date_match = re.findall(r"\b(\d{1,2}[\/\-]\d{1,2}(?:[\/\-]\d{2,4})?)\b", text)
    if date_match:
        entities["dates"] = date_match

    # Time mentions
    time_match = re.findall(r"\b(\d{1,2}(?::\d{2})?\s?(?:am|pm)?)\b", text)
    if time_match:
        entities["times"] = time_match

    # Course codes like “CS101” or “MATH202”
    course_match = re.findall(r"\b[A-Z]{2,4}\d{3}\b", text.upper())
    if course_match:
        entities["course_codes"] = course_match

    # Detect emotional tone keywords
    if any(word in text for word in ["stressed", "anxious", "tired", "motivated", "happy"]):
        entities["emotion_flag"] = True

    return entities


def detect_language(text: str) -> str:
    """Naive language detection for routing to language agents."""
    # MVP heuristic — later replace with langdetect or fastText
    if re.search(r"[áéíóúñ]", text):
        return "spanish"
    elif re.search(r"[äöüß]", text):
        return "german"
    elif re.search(r"[àâçéèêëîïôûùüÿœæ]", text):
        return "french"
    else:
        return "english"


def parse_input(raw_text: str) -> dict:
    """
    Main entry — clean, analyze, and structure the user input.
    Returns a dict used by the Intent Router.
    """
    cleaned = clean_text(raw_text)
    entities = extract_entities(cleaned)
    sentiment = analyze_sentiment(cleaned)
    language = detect_language(cleaned)

    return {
        "original_text": raw_text,
        "cleaned_text": cleaned,
        "entities": entities,
        "language": language,
        "sentiment": sentiment,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
