"""
Peer Collaboration Agent
------------------------
Helps students coordinate and collaborate effectively on group projects,
study sessions, and peer discussions.
"""

from typing import Dict
import random

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for Peer Collaboration Agent.
    Focused on group coordination, communication planning, and study collaboration.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Group project planning
    if any(word in message_lower for word in ["group project", "team project", "collab", "teammates", "members"]):
        response = (
            "To manage a group project effectively:\n"
            "1️⃣ Assign clear roles — leader, researcher, editor, presenter.\n"
            "2️⃣ Set shared deadlines and progress checkpoints.\n"
            "3️⃣ Use a simple tracker (Google Docs, Trello, Notion).\n"
            "4️⃣ Schedule brief sync meetings — 10–15 min daily.\n"
            "Would you like me to generate a task-split plan for your project?"
        )
        suggestions = [
            "Split roles for software engineering project",
            "Create task tracker for group project",
            "Plan weekly progress meeting agenda"
        ]

    # Study groups or joint sessions
    elif any(word in message_lower for word in ["study group", "peer session", "joint study", "collaboration"]):
        response = (
            "Study group coordination tips:\n"
            "• Keep groups small (3–5 members).\n"
            "• Assign one topic per session.\n"
            "• Rotate who explains topics — it boosts retention.\n"
            "• Summarize takeaways at the end of each meet.\n"
            "I can draft a weekly study group schedule — do you want that?"
        )
        suggestions = [
            "Create weekly study group plan",
            "Outline topics to discuss in group sessions",
            "Make group study rotation schedule"
        ]

    # Peer feedback or accountability
    elif any(word in message_lower for word in ["feedback", "review", "peer evaluation", "accountability"]):
        response = (
            "Peer feedback helps both parties improve:\n"
            "1️⃣ Focus feedback on clarity and accuracy, not personal traits.\n"
            "2️⃣ Use ‘Start / Stop / Continue’ feedback structure.\n"
            "3️⃣ For writing: review structure, coherence, and references.\n"
            "Would you like a peer feedback form template?"
        )
        suggestions = [
            "Peer feedback template",
            "Checklist for reviewing classmates' work",
            "How to give constructive feedback"
        ]

    # Communication & conflict management
    elif any(word in message_lower for word in ["conflict", "argument", "disagreement", "team issue", "communication"]):
        response = (
            "Team conflicts happen — handle them with structure:\n"
            "• Address issues early and calmly.\n"
            "• Focus on shared goals, not blame.\n"
            "• Use neutral phrasing like 'Let's find a middle ground.'\n"
            "• Document decisions to avoid confusion later.\n"
            "Would you like a short conflict resolution guide?"
        )
        suggestions = [
            "Conflict resolution checklist",
            "Team communication improvement plan",
            "Sample message for resolving group issues"
        ]

    # Shared resources & file coordination
    elif any(word in message_lower for word in ["shared file", "notes", "drive", "folder", "resources"]):
        response = (
            "To manage shared resources smoothly:\n"
            "1️⃣ Use a structured folder system (by topic or member).\n"
            "2️⃣ Track changes with version history.\n"
            "3️⃣ Store important files in one cloud folder.\n"
            "I can suggest folder naming and sharing templates."
        )
        suggestions = [
            "Create folder structure for group project",
            "Organize shared notes for semester subjects",
            "Suggest collaboration tools"
        ]

    else:
        fallback_responses = [
            "Do you want help organizing a group project or setting up study sessions?",
            "I can help split tasks, plan meetings, or set up a group structure.",
            "Tell me if you need collaboration strategies or team templates."
        ]
        response = random.choice(fallback_responses)

    return {
        "agent": "Peer Collaboration Agent",
        "type": "peer_collaboration",
        "response": response,
        "suggestions": suggestions
    }
