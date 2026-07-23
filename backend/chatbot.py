"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Main Chatbot Controller
Version : 3.0
=========================================================
"""

import re

try:
    from backend.rag import rag_engine
    from backend.ordering import OrderManager
    from backend.memory import memory
except ImportError:
    from rag import rag_engine
    from ordering import OrderManager
    from memory import memory


class CafeChatbot:
    """
    Meeple Cafe AI Chatbot
    """

    def __init__(self):

        self.rag = rag_engine
        self.order = OrderManager()
        self.memory = memory

        self.default_session = "default"

    # =====================================================
    # Save Conversation
    # =====================================================

    def save_user(self, message):

        self.memory.add_message(
            self.default_session,
            "user",
            message
        )

    def save_bot(self, message):

        self.memory.add_message(
            self.default_session,
            "assistant",
            message
        )

    # =====================================================
    # Reply Helper
    # =====================================================

    def reply(self, text):

        self.save_bot(text)

        return text

    # =====================================================
    # Main Chat
    # =====================================================

    def chat(self, user_message):

        try:

            user_message = user_message.strip()

            if not user_message:

                return "Please enter your message."

            self.save_user(user_message)

            message = user_message.lower()

            # =================================================
            # Greetings
            # =================================================

            greetings = [

                "hi",
                "hello",
                "hey",
                "good morning",
                "good afternoon",
                "good evening"

            ]

            if any(
                message == g or message.startswith(g)
                for g in greetings
            ):

                return self.reply(

                    "👋 Welcome to Meeple Cafe!\n\n"

                    "I'm your AI Ordering Assistant.\n\n"

                    "You can ask things like:\n\n"

                    "• Show burgers\n"

                    "• Pizza under ₹300\n"

                    "• Veg pasta\n"

                    "• Cold coffee\n"

                    "• Desserts\n"

                    "• Add Classic Vegetable Stack\n"

                    "• View cart\n"

                    "• Checkout"

                )

            # =================================================
            # Help
            # =================================================

            if message in ["help", "commands"]:

                return self.reply(

                    "📋 Available Commands\n\n"

                    "🍔 Show burgers\n"

                    "🍕 Pizza under ₹300\n"

                    "🥤 Drinks\n"

                    "🍰 Desserts\n"

                    "➕ Add Margherita Pizza\n"

                    "➖ Remove Margherita Pizza\n"

                    "🛒 View cart\n"

                    "🧹 Clear cart\n"

                    "💳 Checkout"

                )

            # =================================================
            # Cart
            # =================================================

            if message in ["cart", "view cart"]:

                return self.reply(
                    self.order.view_cart()
                )

            if message == "checkout":

                return self.reply(
                    self.order.checkout()
                )

            if message == "clear cart":

                self.order.clear_cart()

                return self.reply(
                    "🗑️ Cart cleared successfully."
                )

            # =================================================
            # Add Item
            # =================================================

            add_match = re.search(

                r"add\s+(.+)",

                user_message,

                re.IGNORECASE

            )

            if add_match:

                item = add_match.group(1).strip()

                return self.reply(

                    self.order.add_item(item)

                )

            # =================================================
            # Remove Item
            # =================================================

            remove_match = re.search(

                r"remove\s+(.+)",

                user_message,

                re.IGNORECASE

            )

            if remove_match:

                item = remove_match.group(1).strip()

                return self.reply(

                    self.order.remove_item(item)

                )

            # =================================================
            # AI Search (RAG)
            # =================================================

            response = self.rag.answer(user_message)

            return self.reply(response)

        except Exception as e:

            return (

                "⚠️ Sorry, an unexpected error occurred.\n\n"

                f"{e}"

            )

    # =====================================================
    # Conversation History
    # =====================================================

    def history(self):

        return self.memory.get_history(
            self.default_session
        )

    # =====================================================
    # Clear Conversation
    # =====================================================

    def clear_history(self):

        self.memory.clear_history(
            self.default_session
        )

        return "Conversation history cleared."

    # =====================================================
    # Chat Statistics
    # =====================================================

    def statistics(self):

        return self.memory.statistics()


# =========================================================
# Singleton
# =========================================================

chatbot = CafeChatbot()


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Meeple Cafe AI Ordering Chatbot")
    print("Version 3.0")
    print("=" * 60)
    print("Type 'exit' to quit.\n")

    while True:

        query = input("You : ").strip()

        if query.lower() == "exit":

            print("\n👋 Goodbye!")

            break

        print()

        print("Bot :")

        print(chatbot.chat(query))

        print()
