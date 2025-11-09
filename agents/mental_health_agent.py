"""
Mental Health Agent
-------------------
Handles: stress, motivation, anxiety, and reflective journaling.
Provides CBT-style reasoning and journaling prompts (not therapy).
"""

def handle(user_input: str, context: dict = None) -> str:
    """
    Processes emotional or mental health statements and provides structured reflection.
    """
    text = user_input.lower()

    if any(word in text for word in ["stress", "stressed", "anxious", "anxiety"]):
        return (
            "It sounds like you’re experiencing stress or anxiety. "
            "Try to identify what exactly triggers that feeling — preparation, expectations, or fear of judgment.\n\n"
            "→ Quick exercise: take 3 deep breaths and write down 2 things you can control right now."
        )
    elif any(word in text for word in ["sad", "demotivated", "tired"]):
        return (
            "Feeling low is okay. It might help to take a short walk or write a few sentences "
            "about what’s weighing on your mind. Reflection often reduces the load."
        )
    else:
        return (
            "I’m here to help you think clearly. Try describing what’s bothering you in a bit more detail."
        )
