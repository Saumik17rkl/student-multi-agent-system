"""
Memory Manager
---------------
Simple in-memory session tracker. For MVP, uses Python dict.
Later can be replaced with SQLite or FAISS embeddings for personalization.
"""

from collections import defaultdict

class SessionMemory:
    def __init__(self):
        self.sessions = defaultdict(list)

    def add_message(self, user_id: str, role: str, message: str):
        """Store a message in memory."""
        self.sessions[user_id].append({"role": role, "message": message})

    def get_context(self, user_id: str, limit: int = 5):
        """Return last N messages for conversational context."""
        return self.sessions[user_id][-limit:]

    def clear(self, user_id: str):
        """Reset memory for a specific user."""
        self.sessions[user_id] = []

# Global memory instance
memory = SessionMemory()
