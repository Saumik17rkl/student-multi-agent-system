"""
Error Handlers
--------------
Centralized error handling for the Student Multi-Agent System.
Provides consistent JSON error responses and logging.
"""
from flask import jsonify
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class APIError(Exception):
    """Base exception for API errors"""
    def __init__(self, message: str, status_code: int = 400, payload: Dict[str, Any] = None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload or {}

    def to_dict(self) -> Dict[str, Any]:
        rv = dict(self.payload or {})
        rv['status'] = 'error'
        rv['message'] = self.message
        rv['code'] = self.status_code
        return rv

class ValidationError(APIError):
    """Raised when request validation fails"""
    def __init__(self, message: str = "Invalid request data", payload: Dict[str, Any] = None):
        super().__init__(message, 400, payload)

class UnauthorizedError(APIError):
    """Raised when authentication/authorization fails"""
    def __init__(self, message: str = "Unauthorized", payload: Dict[str, Any] = None):
        super().__init__(message, 401, payload)

class NotFoundError(APIError):
    """Raised when a requested resource is not found"""
    def __init__(self, message: str = "Resource not found", payload: Dict[str, Any] = None):
        super().__init__(message, 404, payload)

class RateLimitExceeded(APIError):
    """Raised when rate limit is exceeded"""
    def __init__(self, message: str = "Rate limit exceeded", payload: Dict[str, Any] = None):
        super().__init__(message, 429, payload)

def handle_api_error(error: APIError):
    """Handle API errors"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

def handle_validation_error(error):
    """Handle validation errors from request parsing"""
    return jsonify({
        'status': 'error',
        'code': 400,
        'message': 'Validation error',
        'errors': error.messages
    }), 400

def handle_404_error(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'code': 404,
        'message': 'The requested URL was not found on the server.'
    }), 404

def handle_500_error(error):
    """Handle 500 errors"""
    logger.exception("Internal server error: %s", error)
    return jsonify({
        'status': 'error',
        'code': 500,
        'message': 'An internal server error occurred.'
    }), 500

def handle_generic_exception(error):
    """Handle all other uncaught exceptions"""
    logger.exception("Unhandled exception: %s", error)
    return jsonify({
        'status': 'error',
        'code': 500,
        'message': 'An unexpected error occurred.'
    }), 500

def register_error_handlers(app):
    """Register all error handlers with the Flask app"""
    app.errorhandler(APIError)(handle_api_error)
    app.errorhandler(400)(handle_validation_error)
    app.errorhandler(404)(handle_404_error)
    app.errorhandler(500)(handle_500_error)
    app.errorhandler(Exception)(handle_generic_exception)