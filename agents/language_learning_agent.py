"""
Language Learning Agent
-----------------------
Helps students improve grammar, vocabulary, and general language skills.
Provides corrections, example sentences, and quick vocabulary quizzes.
"""

from typing import Dict
import random
import re

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for Language Learning Agent.
    Handles grammar correction, vocabulary building, and quiz-style exercises.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Grammar correction
    if any(word in message_lower for word in ["fix grammar", "correct sentence", "grammar check", "proofread"]):
        corrected = grammar_correction_mock(message)
        response = (
            f"Here's the corrected version of your text:\n\n✅ **{corrected}**\n\n"
            "Remember — focus on subject-verb agreement and article usage!"
        )
        suggestions = [
            "Check grammar for this sentence: 'She go to school every day.'",
            "Fix punctuation errors in my paragraph.",
            "Proofread my email for mistakes."
        ]

    # Vocabulary quiz
    elif any(word in message_lower for word in ["vocabulary", "quiz", "word test", "new words"]):
        quiz = random.choice(vocabulary_quiz_bank())
        response = (
            f"🧠 **Vocabulary Challenge!**\n"
            f"Word: *{quiz['word']}*\n"
            f"Choose the correct meaning:\n"
            f"A. {quiz['options'][0]}\n"
            f"B. {quiz['options'][1]}\n"
            f"C. {quiz['options'][2]}"
        )
        suggestions = [
            "Give me another vocabulary quiz!",
            "Teach me 5 new English words.",
            "Explain the difference between 'affect' and 'effect'."
        ]

    # Learning advice
    elif any(word in message_lower for word in ["improve english", "learn vocabulary", "speak better", "language tips"]):
        response = (
            "To improve your language skills:\n"
            "1️⃣ Read short news articles daily.\n"
            "2️⃣ Keep a vocabulary journal.\n"
            "3️⃣ Record yourself speaking and review pronunciation.\n"
            "4️⃣ Use flashcards for spaced repetition.\n"
            "Want me to make a 7-day learning plan for you?"
        )
        suggestions = [
            "Create a 7-day English improvement plan",
            "Daily vocabulary practice routine",
            "Reading comprehension exercises"
        ]

    else:
        fallback_responses = [
            "Would you like me to check grammar, suggest vocabulary, or test you with a quiz?",
            "I can proofread, teach words, or make mini language tests.",
            "Need help improving English writing or speaking?"
        ]
        response = random.choice(fallback_responses)

    return {
        "agent": "Language Learning Agent",
        "type": "language_learning",
        "response": response,
        "suggestions": suggestions
    }

# ---------------- Mock Grammar Fix ---------------- #
def grammar_correction_mock(text: str) -> str:
    """
    Very basic mock grammar correction (no ML, just sample transformation).
    In production: use LanguageTool, Grammarly API, or LLM.
    """
    text = re.sub(r"\bshe go\b", "she goes", text, flags=re.I)
    text = re.sub(r"\bhe go\b", "he goes", text, flags=re.I)
    text = re.sub(r"\bi is\b", "I am", text, flags=re.I)
    return text.strip().capitalize()

# ---------------- Quiz Bank ---------------- #
def vocabulary_quiz_bank():
    """Returns a small sample of quiz questions."""
    return [
        {"word": "Eloquent", "options": ["Well-spoken", "Silent", "Confused"]},
        {"word": "Pragmatic", "options": ["Practical", "Emotional", "Unrealistic"]},
        {"word": "Ambiguous", "options": ["Unclear", "Definite", "Easy"]},
        {"word": "Meticulous", "options": ["Careful", "Careless", "Fast"]},
        {"word": "Concur", "options": ["Agree", "Argue", "Ignore"]}
    ]
