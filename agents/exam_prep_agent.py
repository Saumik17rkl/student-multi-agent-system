"""
Exam Prep Agent
---------------
This agent helps students prepare for exams — providing study strategies,
sample questions, revision plans, and topic breakdowns.
"""

from typing import Dict
import random

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for Exam Prep Agent.
    Detects whether the student wants revision help, mock questions, study plans, or strategies.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Detect exam-related intent
    if any(word in message_lower for word in ["exam", "test", "quiz", "mock", "practice"]):
        response = (
            "Exam preparation essentials:\n"
            "1️⃣ Review your syllabus and identify weak areas.\n"
            "2️⃣ Study in 45–50 minute focused blocks (Pomodoro method).\n"
            "3️⃣ Revise key formulas or definitions daily.\n"
            "4️⃣ Attempt mock questions under timed conditions.\n"
            "Would you like me to generate a small quiz for your topic?"
        )
        suggestions = [
            "Create a quiz on computer networks",
            "Make a study checklist for physics exam",
            "Tips to handle test anxiety"
        ]

    elif any(word in message_lower for word in ["study plan", "revision", "schedule", "routine"]):
        response = (
            "Here’s a solid revision structure:\n"
            "• Morning: Concept review (new material)\n"
            "• Afternoon: Practice problems or quizzes\n"
            "• Evening: Summarize what you learned + flashcards\n"
            "• Night: Quick recap (no new topics)\n"
            "I can build a 3-day or 7-day plan if you share your exam date."
        )
        suggestions = [
            "Generate 3-day revision plan for calculus",
            "Make weekly study schedule for finals",
            "Optimize my study time for multiple subjects"
        ]

    elif any(word in message_lower for word in ["formula", "definition", "key terms", "short notes"]):
        response = (
            "Revision technique:\n"
            "1️⃣ Create flashcards for key formulas or terms.\n"
            "2️⃣ Use spaced repetition (Anki or manual review).\n"
            "3️⃣ Group related terms by chapter.\n"
            "Would you like me to generate a short-notes format for your topic?"
        )
        suggestions = [
            "Generate short notes for thermodynamics",
            "List important formulas for statistics",
            "Make flashcards for biology definitions"
        ]

    elif any(word in message_lower for word in ["time management", "focus", "memory", "retention"]):
        response = (
            "To improve focus and memory:\n"
            "• Avoid multitasking during study sessions.\n"
            "• Use active recall instead of rereading.\n"
            "• Take 5–10 min breaks every 45 minutes.\n"
            "• Sleep 7–8 hours before exams for optimal retention.\n"
            "Would you like a focus improvement checklist?"
        )
        suggestions = [
            "Focus improvement checklist",
            "Memory retention methods",
            "Effective revision strategy"
        ]

    elif any(word in message_lower for word in ["question", "mcq", "sample", "practice problems"]):
        response = (
            "I can generate custom sample questions or MCQs for your subject.\n"
            "Just specify your topic — for example:\n"
            "‘Generate 5 MCQs on sorting algorithms’ or ‘Ask me Python loops questions’."
        )
        suggestions = [
            "Generate 5 MCQs on data structures",
            "Create short answer questions on world history",
            "Make a timed quiz for chemistry basics"
        ]

    else:
        fallback_responses = [
            "Can you tell me which subject or exam you're preparing for?",
            "I can help with revision plans, quizzes, or memory tips — what do you need?",
            "Would you like a daily exam preparation routine?"
        ]
        response = random.choice(fallback_responses)

    return {
        "agent": "Exam Prep Agent",
        "type": "exam_prep",
        "response": response,
        "suggestions": suggestions
    }
