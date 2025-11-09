"""
Intent Router
-------------
Routes user input to the appropriate sub-agent based on detected intent.
Uses keyword-based routing for MVP (replace with fine-tuned model later).
"""

from agents import (
    academic_agent,
    productivity_agent,
    mental_health_agent,
    admin_finance_agent,
    career_guidance_agent,
    peer_collaboration_agent,
    language_learning_agent,
    health_lifestyle_agent,
    feedback_evaluation_agent,
    library_resources_agent
)

def detect_intent(text: str) -> str:
    """Lightweight rule-based intent classifier."""
    text = text.lower()

    if any(word in text for word in ["study", "explain", "assignment", "topic", "lecture", "exam", "concept"]):
        return "academic"
    elif any(word in text for word in ["schedule", "remind", "plan", "deadline", "time management", "to-do", "calendar"]):
        return "productivity"
    elif any(word in text for word in ["career", "job", "internship", "resume", "cover letter", "interview"]):
        return "career"
    elif any(word in text for word in ["stress", "anxious", "sad", "motivation", "burnout", "overwhelmed", "focus"]):
        return "mental_health"
    elif any(word in text for word in ["scholarship", "register", "fee", "budget", "form", "finance", "admin"]):
        return "admin_finance"
    elif any(word in text for word in ["textbook", "book", "reading material", "journal", "reference", "research", "paper", "citation"]):
        return "library_resources"
    elif any(word in text for word in ["feedback", "evaluation", "course feedback", "teacher rating", "improvement"]):
        return "feedback_evaluation"
    elif any(word in text for word in ["language", "translation", "grammar", "accent", "vocabulary", "learn english", "speak better"]):
        return "language_learning"
    elif any(word in text for word in ["collaborate", "group project", "study group", "peer", "teamwork", "discussion"]):
        return "peer_collaboration"
    elif any(word in text for word in ["sleep", "insomnia", "tired", "diet", "exercise", "hydration", "workout", "lifestyle"]):
        return "health_lifestyle"
    else:
        return "unknown"


def route_to_agent(intent: str, text: str, context: dict = None) -> dict:
    """Dispatch query to the correct specialized agent."""
    if context is None:
        context = {}

    # Ensure we always return a dictionary with at least a 'response' key
    try:
        if intent == "academic":
            result = academic_agent.handle_query(text, context)
            if not isinstance(result, dict) or 'response' not in result:
                return {"response": str(result) if result else "I'm not sure how to respond to that.", "context": context}
            return result
            
        # For other agents, ensure they return a dictionary with a 'response' key
        agent_response = None
        if intent == "productivity":
            agent_response = productivity_agent.handle(text, context)
        elif intent == "career":
            agent_response = career_guidance_agent.handle(text, context)
        elif intent == "mental_health":
            agent_response = mental_health_agent.handle(text, context)
        elif intent == "admin_finance":
            agent_response = admin_finance_agent.handle(text, context)
        elif intent == "library_resources":
            agent_response = library_resources_agent.handle(text, context)
        elif intent == "feedback_evaluation":
            agent_response = feedback_evaluation_agent.handle(text, context)
        elif intent == "language_learning":
            agent_response = language_learning_agent.handle(text, context)
        elif intent == "peer_collaboration":
            agent_response = peer_collaboration_agent.handle(text, context)
        elif intent == "health_lifestyle":
            agent_response = health_lifestyle_agent.handle(text, context)
        else:
            return {"response": "I'm not sure how to handle that request. Could you rephrase?", "context": context}

        # Ensure the response is properly formatted
        if isinstance(agent_response, dict):
            if 'response' not in agent_response:
                agent_response['response'] = str(agent_response.get('message', 'I processed your request.'))
            if 'context' not in agent_response:
                agent_response['context'] = context
            return agent_response
            
        return {
            "response": str(agent_response) if agent_response else "I'm not sure how to respond to that.", 
            "context": context
        }

    except Exception as e:
        return {
            "response": f"An error occurred while processing your request: {str(e)}", 
            "context": context, 
            "error": True,
            "agent": "ErrorHandler",
            "suggestions": ["Try rephrasing your question", "Contact support if the issue persists"]
        }
