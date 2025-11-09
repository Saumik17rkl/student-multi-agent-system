"""
Chat Routes
------------
Defines endpoints for user-AI interactions.
Uses Flask Blueprint so routes can be easily registered in app.py.
"""

from flask import Blueprint, request, jsonify
import time
from core import parser, intent_router, response_composer, memory_manager
from utils.error_handlers import ValidationError, APIError
import logging

# Logging setup
logger = logging.getLogger(__name__)

chat_bp = Blueprint("chat_bp", __name__)

# ---------------------------
# /chat Endpoint
# ---------------------------
@chat_bp.route("/chat", methods=["POST"])
def handle_chat():
    """
    POST /chat
    Body: { "user_id": "string", "message": "text input" }
    Returns: JSON with detected intent, routed agent, structured response, and conversation history.
    """
    start_time = time.time()
    try:
        data = request.get_json(force=True)
        user_id = data.get("user_id", "anonymous").strip()
        user_message = data.get("message", "").strip()

        if not user_message:
            raise ValidationError("Message cannot be empty")

        # Log incoming message
        memory_manager.memory.add_message(user_id, "user", user_message)

        # Step 1. Clean and parse
        parsed = parser.parse_input(user_message)

        # Step 2. Detect intent
        intent = intent_router.detect_intent(parsed["cleaned_text"])

        # Step 3. Route to correct sub-agent
        agent_output = intent_router.route_to_agent(intent, parsed["cleaned_text"])

        # Step 4. Compose structured response
        composed = response_composer.compose_response(intent, agent_output)

        # Step 5. Save AI reply
        memory_manager.memory.add_message(user_id, "assistant", composed)

        # Step 6. Return structured JSON
        elapsed = round(time.time() - start_time, 3)
        return jsonify({
            "status": "success",
            "intent": intent,
            "language": parsed.get("language", "unknown"),
            "entities": parsed.get("entities", {}),
            "sentiment": parsed.get("sentiment", {}),
            "response": composed,
            "elapsed_time_sec": elapsed,
            "history": memory_manager.memory.get_context(user_id)
        }), 200

    except ValidationError as e:
        raise e
    except Exception as e:
        logger.exception("Error in /chat endpoint")
        raise APIError(str(e), 500)

# ---------------------------
# /clear Endpoint
# ---------------------------
@chat_bp.route("/clear", methods=["POST"])
def clear_memory():
    """
    POST /clear
    Body: { "user_id": "string" }
    Clears memory for the specified user.
    """
    try:
        data = request.get_json(force=True)
        user_id = data.get("user_id", "anonymous").strip()
        memory_manager.memory.clear(user_id)
        return jsonify({"status": "success", "message": f"Session memory cleared for {user_id}."})
    except Exception as e:
        logger.exception("Error in /clear endpoint")
        raise APIError(str(e), 500)

# ---------------------------
# /health Endpoint
# ---------------------------
@chat_bp.route("/health", methods=["GET"])
def health_check():
    """Simple endpoint to confirm the server is running."""
    return jsonify({
        "status": "ok",
        "system": "Student Multi-Agent System API",
        "agents_active": 13,
        "message": "Service running and healthy."
    })
