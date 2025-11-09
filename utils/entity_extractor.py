"""
Entity Extractor Utility
------------------------
Extracts meaningful entities (course, dates, keywords) for intent routing.
Used by Academic, Admin, and Finance agents.
"""

import re

def extract_entities(text: str) -> dict:
    """
    Extracts high-level academic or admin entities.
    """
    entities = {}

    # Course name or subject
    match_course = re.search(r"\b(cs|math|physics|biology|history|english|chemistry)\b", text.lower())
    if match_course:
        entities["course"] = match_course.group()

    # Detect numbers as possible dates
    match_date = re.findall(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", text)
    if match_date:
        entities["date"] = match_date[0]

    # Detect keywords for scholarships, forms, exams
    if "scholarship" in text.lower():
        entities["keyword"] = "scholarship"
    elif "exam" in text.lower():
        entities["keyword"] = "exam"
    elif "assignment" in text.lower():
        entities["keyword"] = "assignment"

    return entities
