"""
Student Multi-Agent Architect & Builder
---------------------------------------
Main Flask entry point for the student problem-solving AI system.

This orchestrates:
 - Input parsing
 - Intent routing
 - Agent handling
 - Response composition
 - Session memory management

Author: God of Prompt Systems
"""

from flask import Flask, jsonify
from flask_cors import CORS
import logging
from routes.chat_routes import chat_bp
from config import APP_NAME, VERSION
from dotenv import load_dotenv
load_dotenv()



# ------------------------------------------------------
# Flask App Initialization
# ------------------------------------------------------
app = Flask(__name__)
CORS(app)  # Enables access from frontend apps like React, Streamlit, etc.
app.register_blueprint(chat_bp)

# ------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(APP_NAME)


# ------------------------------------------------------
# Root Health Check
# ------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    """Root endpoint to verify API is running."""
    logger.info("Root health check accessed.")
    return jsonify({
        "status": "running",
        "app": APP_NAME,
        "version": VERSION,
        "message": "Welcome to the Student Multi-Agent Architect & Builder API"
    })


# ------------------------------------------------------
# Error Handlers
# ------------------------------------------------------
@app.errorhandler(404)
def handle_404(error):
    """Handles non-existent endpoints gracefully."""
    logger.warning("404 - Endpoint not found: %s", error)
    return jsonify({
        "error": "Endpoint not found",
        "code": 404
    }), 404


@app.errorhandler(500)
def handle_500(error):
    """Handles internal server errors."""
    logger.exception("500 - Internal Server Error: %s", error)
    return jsonify({
        "error": "Internal server error",
        "code": 500
    }), 500


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    """Catch-all for any unhandled exceptions."""
    logger.exception("Unhandled exception occurred: %s", error)
    return jsonify({
        "error": "Unexpected server error",
        "message": str(error)
    }), 500


# ------------------------------------------------------
# Startup Hook
# ------------------------------------------------------
@app.before_request
def init_system_once():
    if not getattr(app, "_initialized", False):
        app._initialized = True
        """Logs when the app successfully starts."""
        logger.info(f"✅ {APP_NAME} (v{VERSION}) initialized and ready to serve requests.")

# ------------------------------------------------------
# Entry Point
# ------------------------------------------------------
if __name__ == "__main__":
    logger.info(f"🚀 Launching {APP_NAME} (v{VERSION}) on http://0.0.0.0:5000")
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
