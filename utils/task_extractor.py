"""
Task Extractor Utility
----------------------
Extracts structured task information from natural language text.
Used primarily by Productivity Agent.
"""

import re
from datetime import datetime, timedelta

def extract_tasks(text: str):
    """
    Parse common task-related phrases like:
    - "finish 3 assignments by Friday"
    - "submit project tomorrow"
    """
    tasks = []
    date_keywords = ["today", "tomorrow", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    # Detect numbers and action verbs
    numbers = re.findall(r"\b\d+\b", text)
    verbs = re.findall(r"\b(finish|submit|complete|do|write|plan|study|review)\b", text.lower())

    # Detect date references
    dates = [word for word in text.lower().split() if word in date_keywords]

    task = {
        "action": verbs[0] if verbs else "task",
        "quantity": numbers[0] if numbers else None,
        "due": dates[0] if dates else "unspecified"
    }

    tasks.append(task)
    return tasks
