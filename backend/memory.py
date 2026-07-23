"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Conversation Memory
Version : 3.0
=========================================================
"""

from collections import defaultdict
from datetime import datetime
from typing import Dict, List


class ConversationMemory:
    """
    Conversation Memory

    Features
    --------
    ✔ Store chat history per session
    ✔ Retrieve conversation history
    ✔ Clear history
    ✔ Keep only recent messages
    ✔ Simple conversation summary
    """

    def __init__(self, max_messages: int = 20):

        self.max_messages = max_messages

        self.memory: Dict[str, List[dict]] = defaultdict(list)

    # =====================================================
    # Add Message
    # =====================================================

    def add_message(
        self,
        session_id: str,
        role: str,
        message: str
    ):

        self.memory[session_id].append(
            {
                "role": role,
                "message": message,
                "timestamp": datetime.now().isoformat()
            }
        )

        if len(self.memory[session_id]) > self.max_messages:

            self.memory[session_id] = self.memory[session_id][
                -self.max_messages:
            ]

    # =====================================================
    # Get History
    # =====================================================

    def get_history(self, session_id: str):

        return self.memory.get(session_id, [])

    # =====================================================
    # Get Last N Messages
    # =====================================================

    def get_recent_messages(
        self,
        session_id: str,
        limit: int = 5
    ):

        history = self.memory.get(session_id, [])

        return history[-limit:]

    # =====================================================
    # Build Context
    # =====================================================

    def build_context(
        self,
        session_id: str,
        limit: int = 6
    ):

        history = self.get_recent_messages(session_id, limit)

        if not history:
            return ""

        context = []

        for item in history:

            context.append(
                f"{item['role'].capitalize()}: {item['message']}"
            )

        return "\n".join(context)

    # =====================================================
    # Clear Session
    # =====================================================

    def clear_history(self, session_id: str):

        if session_id in self.memory:

            del self.memory[session_id]

    # =====================================================
    # Delete One Message
    # =====================================================

    def remove_last_message(self, session_id: str):

        if (
            session_id in self.memory
            and self.memory[session_id]
        ):

            self.memory[session_id].pop()

    # =====================================================
    # Session Exists
    # =====================================================

    def has_session(self, session_id: str):

        return session_id in self.memory

    # =====================================================
    # Total Sessions
    # =====================================================

    def total_sessions(self):

        return len(self.memory)

    # =====================================================
    # Total Messages
    # =====================================================

    def total_messages(self):

        total = 0

        for history in self.memory.values():

            total += len(history)

        return total

    # =====================================================
    # Statistics
    # =====================================================

    def statistics(self):

        return {

            "sessions": self.total_sessions(),

            "messages": self.total_messages(),

            "max_messages_per_session": self.max_messages

        }

    # =====================================================
    # Summary
    # =====================================================

    def summarize(self, session_id: str):

        history = self.get_history(session_id)

        if not history:

            return "No conversation."

        lines = []

        for item in history:

            lines.append(
                f"{item['role']}: {item['message']}"
            )

        return "\n".join(lines)


# =========================================================
# Singleton
# =========================================================

memory = ConversationMemory()
