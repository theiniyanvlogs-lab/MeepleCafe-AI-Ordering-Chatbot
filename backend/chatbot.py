"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Chatbot Controller
Version : 1.0
=========================================================
"""

from search_engine import MenuSearchEngine
from ordering import OrderManager
from memory import ConversationMemory


class RestaurantChatbot:
    """
    Main Chatbot Controller

    Responsibilities
    ----------------
    1. Greeting
    2. Menu Search
    3. Recommendation
    4. Cart Management
    5. Checkout
    6. FAQ
    """

    def __init__(self):

        self.search = MenuSearchEngine()
        self.order = OrderManager()
        self.memory = ConversationMemory()

    # ----------------------------------------------------

    def get_response(self, message: str, session_id: str = "guest"):

        message = message.strip()

        if not message:
            return "Please type your question."

        lower = message.lower()

        # ------------------------------------------
        # Greetings
        # ------------------------------------------

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening"
        ]

        if lower in greetings:

            return (
                "👋 Welcome to Meeple Cafe!\n\n"
                "How can I help you today?\n\n"
                "🍔 Burgers\n"
                "🍕 Pizza\n"
                "☕ Coffee\n"
                "🥤 Shakes\n"
                "🍟 Snacks\n"
                "🍝 Pasta"
            )

        # ------------------------------------------
        # View Cart
        # ------------------------------------------

        if "cart" in lower:

            return self.order.view_cart(session_id)

        # ------------------------------------------
        # Checkout
        # ------------------------------------------

        if "checkout" in lower:

            return self.order.checkout(session_id)

        # ------------------------------------------
        # Add Item
        # ------------------------------------------

        if lower.startswith("add "):

            item_name = message[4:]

            return self.order.add_item(
                session_id,
                item_name
            )

        # ------------------------------------------
        # Remove Item
        # ------------------------------------------

        if lower.startswith("remove "):

            item_name = message[7:]

            return self.order.remove_item(
                session_id,
                item_name
            )

        # ------------------------------------------
        # Menu Search
        # ------------------------------------------

        result = self.search.search(message)

        if result:
            return result

        # ------------------------------------------
        # Default
        # ------------------------------------------

        return (
            "Sorry, I couldn't understand your request.\n\n"
            "Try asking:\n"
            "• Show Burgers\n"
            "• Show Pizza\n"
            "• Coffee below ₹200\n"
            "• Veg Pasta\n"
            "• Add Burger\n"
            "• View Cart"
        )
