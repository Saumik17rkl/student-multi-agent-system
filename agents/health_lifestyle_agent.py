"""
Health & Lifestyle Agent
------------------------
Supports student wellness by offering sleep optimization tips,
workout suggestions, hydration tracking, and daily health reminders.
"""

from typing import Dict
import random
import datetime

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for Health & Lifestyle Agent.
    Detects lifestyle-related queries and gives structured, actionable advice.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Sleep-related queries
    if any(word in message_lower for word in ["sleep", "insomnia", "tired", "rest", "bedtime"]):
        response = (
            "🛌 Sleep Optimization Tips:\n"
            "1️⃣ Maintain a consistent bedtime — even on weekends.\n"
            "2️⃣ Avoid screens 45 minutes before sleeping.\n"
            "3️⃣ Try 4-7-8 breathing before bed.\n"
            "4️⃣ Keep your room cool (around 19°C / 66°F).\n"
            "Would you like me to create a 7-day sleep improvement plan?"
        )
        suggestions = [
            "Generate a 7-day sleep routine",
            "Suggest nighttime relaxation exercises",
            "Track sleep hours for this week"
        ]

    # Workout queries
    elif any(word in message_lower for word in ["workout", "exercise", "fitness", "training", "gym", "run", "yoga"]):
        workouts = [
            "10-minute morning stretch + 15 squats + 20 pushups + 1 km jog",
            "15 min yoga session + breathing exercises",
            "Full-body home workout: 3×20 squats, 3×15 push-ups, 3×30 sec planks",
            "HIIT routine: 40 sec jumping jacks, 20 sec rest, repeat 5 times"
        ]
        routine = random.choice(workouts)
        response = f"💪 Here’s a workout suggestion for today:\n{routine}\nWant me to create a 3-day or 7-day fitness plan?"
        suggestions = [
            "Plan 3-day beginner workout schedule",
            "Suggest yoga routine for relaxation",
            "Track calories or hydration after exercise"
        ]

    # Hydration tracking
    elif any(word in message_lower for word in ["water", "hydration", "drink", "thirst"]):
        now = datetime.datetime.now().strftime("%H:%M")
        response = (
            f"💧 Hydration Check ({now}):\n"
            "Aim for 2–3 liters of water daily (≈ 8–10 cups).\n"
            "Drink one glass every 2 hours and more after exercise.\n"
            "Would you like me to remind you every 2 hours to drink water?"
        )
        suggestions = [
            "Set hydration reminders",
            "Track daily water intake",
            "Calculate recommended hydration level"
        ]

    # Nutrition or lifestyle balance
    elif any(word in message_lower for word in ["diet", "nutrition", "food", "eat healthy", "meal plan"]):
        response = (
            "🍎 Quick Nutrition Advice:\n"
            "• Balance your plate: half veggies, quarter protein, quarter carbs.\n"
            "• Avoid skipping breakfast — it affects focus.\n"
            "• Stay hydrated and include fruits twice a day.\n"
            "Would you like me to suggest a simple 3-meal daily plan?"
        )
        suggestions = [
            "Make 3-day healthy meal plan",
            "Suggest quick energy snacks for study breaks",
            "Recommend vegetarian protein options"
        ]

    else:
        fallback = [
            "Need help improving sleep, workout plans, or hydration tracking?",
            "I can make simple routines for rest, exercise, and water reminders.",
            "Would you like a daily health check-in setup?"
        ]
        response = random.choice(fallback)

    return {
        "agent": "Health & Lifestyle Agent",
        "type": "health_lifestyle",
        "response": response,
        "suggestions": suggestions
    }
