"""
Career Guidance Agent
---------------------
This sub-agent helps students with career development:
resume feedback, internship search guidance, skill-building, and job prep advice.
"""

from typing import Dict
import random

def handle(message: str, context: Dict = None) -> Dict:
    """
    Main handler for the Career Guidance Agent.
    Determines intent type (resume help, job search, skill advice, etc.)
    and generates an appropriate response.
    """

    message_lower = message.lower()
    response = ""
    suggestions = []

    # Detect type of career-related query
    if any(word in message_lower for word in ["resume", "cv", "cover letter"]):
        response = (
            "Here's a quick checklist to improve your resume:\n"
            "1️⃣ Keep it concise (1 page for undergrads).\n"
            "2️⃣ Focus on measurable achievements, not just responsibilities.\n"
            "3️⃣ Tailor it for each job/internship.\n"
            "4️⃣ Use action verbs like 'developed', 'led', 'analyzed'.\n"
            "Would you like me to format or review a specific section?"
        )
        suggestions = [
            "Review my resume summary",
            "Help me rewrite my project descriptions",
            "What should I include in my cover letter?"
        ]

    elif any(word in message_lower for word in ["internship", "intern", "placement"]):
        response = (
            "Internship hunt strategy:\n"
            "1️⃣ Start with your university’s placement portal or LinkedIn Jobs.\n"
            "2️⃣ Target companies offering roles in your field of study.\n"
            "3️⃣ Prepare a short pitch about your skills and motivation.\n"
            "4️⃣ Apply early — competition peaks mid-semester.\n"
            "Do you want a list of platforms or current openings in your field?"
        )
        suggestions = [
            "List top internship sites for CS students",
            "How do I write an internship email?",
            "What skills do recruiters look for in interns?"
        ]

    elif any(word in message_lower for word in ["career", "job", "profession", "path"]):
        response = (
            "Career exploration guide:\n"
            "1️⃣ Identify what you enjoy doing most academically or in projects.\n"
            "2️⃣ Research related career paths (I can list some if you tell me your major).\n"
            "3️⃣ Check current job trends and skill requirements.\n"
            "4️⃣ Build a roadmap — courses, certifications, and experiences.\n"
            "Would you like me to generate a personalized roadmap?"
        )
        suggestions = [
            "Suggest career paths for Data Science",
            "What jobs can I get after Computer Engineering?",
            "Generate a career roadmap for UI/UX design"
        ]

    elif any(word in message_lower for word in ["skill", "learn", "improve", "develop"]):
        response = (
            "To grow your skills effectively:\n"
            "1️⃣ Focus on one technical and one soft skill each month.\n"
            "2️⃣ Use Coursera, edX, or freeCodeCamp for guided learning.\n"
            "3️⃣ Practice with real projects or GitHub contributions.\n"
            "4️⃣ Track your progress weekly.\n"
            "Would you like me to suggest a learning plan for a specific role?"
        )
        suggestions = [
            "Skill roadmap for backend developer",
            "Soft skills important for interviews",
            "How to learn project management effectively"
        ]

    elif any(word in message_lower for word in ["interview", "prep", "practice", "questions"]):
        response = (
            "Interview preparation basics:\n"
            "1️⃣ Review your resume — expect questions from your listed work.\n"
            "2️⃣ Practice common technical + behavioral questions.\n"
            "3️⃣ Research the company thoroughly.\n"
            "4️⃣ Prepare a 30-second self-introduction (elevator pitch).\n"
            "Do you want a list of top interview questions for your role?"
        )
        suggestions = [
            "Top behavioral interview questions",
            "Mock interview for software engineer",
            "How to answer 'Tell me about yourself'"
        ]

    else:
        fallback_responses = [
            "Can you clarify your career goal? (e.g., 'Find internships in AI', 'Help improve my resume')",
            "I can assist with career paths, resumes, interviews, or skills. What should we focus on first?",
            "Let's talk about your career direction — what's your target field or job role?"
        ]
        response = random.choice(fallback_responses)

    return {
        "agent": "Career Guidance Agent",
        "type": "career_guidance",
        "response": response,
        "suggestions": suggestions
    }
