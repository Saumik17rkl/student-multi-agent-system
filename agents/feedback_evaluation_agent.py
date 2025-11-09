"""
Feedback & Evaluation Agent
---------------------------
Helps students gather, organize, and reflect on feedback
for courses, assignments, and personal skill development.
Also supports self-evaluation prompts and progress tracking.
"""

from typing import Dict
import random
import datetime

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for Feedback & Evaluation Agent.
    Detects feedback collection, progress review, and improvement tracking queries.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Course feedback collection
    if any(word in message_lower for word in ["course feedback", "class feedback", "professor", "teacher rating"]):
        response = (
            "📋 Here’s a course feedback template you can use:\n"
            "1️⃣ What worked well in the course?\n"
            "2️⃣ What could be improved?\n"
            "3️⃣ How effective were the assignments?\n"
            "4️⃣ Was communication clear and timely?\n"
            "Would you like me to generate a feedback form in text or Google Form format?"
        )
        suggestions = [
            "Generate feedback form for course review",
            "Summarize student feedback data",
            "Write polite constructive feedback for a professor"
        ]

    # Assignment or project evaluation
    elif any(word in message_lower for word in ["assignment feedback", "project review", "peer evaluation"]):
        response = (
            "📑 Here’s a framework for evaluating assignments:\n"
            "• Clarity and structure (Is it easy to follow?)\n"
            "• Depth of analysis (Did it go beyond surface-level?)\n"
            "• Technical accuracy (Any errors or inconsistencies?)\n"
            "• Presentation and formatting\n"
            "Would you like me to create a rubric for this project?"
        )
        suggestions = [
            "Create grading rubric for project",
            "Summarize peer feedback notes",
            "Track assignment improvement over time"
        ]

    # Personal reflection and improvement tracking
    elif any(word in message_lower for word in ["self-evaluation", "improvement", "reflect", "progress", "goals"]):
        today = datetime.date.today().strftime("%B %d, %Y")
        response = (
            f"📆 **Self-Reflection Template ({today})**\n"
            "1️⃣ What went well this week?\n"
            "2️⃣ What could you have done better?\n"
            "3️⃣ What’s one goal for next week?\n"
            "4️⃣ Rate your productivity (1–10)\n"
            "Would you like me to record and track these reflections weekly?"
        )
        suggestions = [
            "Start weekly reflection log",
            "Summarize monthly progress",
            "Track improvements across semesters"
        ]

    # Feedback analysis and summary
    elif any(word in message_lower for word in ["analyze feedback", "summary", "trends", "improvement report"]):
        response = (
            "📊 Feedback Summary Steps:\n"
            "1️⃣ Group responses into themes (positives, challenges, suggestions).\n"
            "2️⃣ Calculate average ratings if quantitative.\n"
            "3️⃣ Identify top 3 areas for improvement.\n"
            "4️⃣ Write 1-paragraph summary with actionable insights.\n"
            "Would you like a sample feedback summary format?"
        )
        suggestions = [
            "Generate summary of collected feedback",
            "Highlight top improvement areas",
            "Visualize feedback trends"
        ]

    else:
        fallback = [
            "Would you like to collect feedback, analyze it, or reflect on your own progress?",
            "I can generate templates, summaries, or improvement trackers.",
            "Need help writing constructive feedback or self-evaluation?"
        ]
        response = random.choice(fallback)

    return {
        "agent": "Feedback & Evaluation Agent",
        "type": "feedback_evaluation",
        "response": response,
        "suggestions": suggestions
    }
