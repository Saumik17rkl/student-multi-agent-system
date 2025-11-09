"""
Text Cleaner Utility
--------------------
Removes extra characters, normalizes whitespace, and standardizes user input.
"""

import re

def clean_text(text: str) -> str:
    """Normalize and sanitize user input text."""
    if not text:
        return ""
    text = text.strip().lower()
    text = re.sub(r"[^a-zA-Z0-9\s.,!?'-]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text
