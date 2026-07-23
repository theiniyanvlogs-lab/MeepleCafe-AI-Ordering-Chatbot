"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Main Chatbot Controller
Version : 1.0
=========================================================
"""

import re

from rag import RAGEngine
from ordering import OrderManager
from memory import ConversationMemory


class CafeChatbot:
    """
    Main AI Chatbot Controller
    """

    def __init__(self):

        self.rag = RAGEngine()
        self.order = OrderManager()
        self.memory = ConversationMemory()

    # =====================================================
    # Main Chat Function
    # =====================================================

    def chat(self, user_message):

        user_message = user_message.strip()

        if not user_message:
            return "Please enter your message."

        self.memory.add_user_message(user_message)

        message = user_message.lower()

        # ---------------------------------------------
        # Greetings
        # ---------------------------------------------

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening"
        ]

        if any(g in message for g in greetings):

            reply = (
                "👋 Welcome to Meeple Cafe!\n\n"
                "How may I help you today?\n\n"
                "You can ask things like:\n"
                "• Show burgers\n"
                "• Pizza under ₹300\n"
                "• Do you have desserts?\n"
                "• Add Margherita Pizza\n"
                "• View cart"
            )

            self.memory.add_bot_message(reply)
            return reply

        # ---------------------------------------------
        # View Cart
        # ---------------------------------------------

        if "view cart" in message or "cart" == message:

            cart = self.order.view_cart()

            self.memory.add_bot_message(cart)

            return cart

        # ---------------------------------------------
        # Checkout
        # ---------------------------------------------

        if "checkout" in message:

            result = self.order.checkout()

            self.memory.add_bot_message(result)

            return result

        # ---------------------------------------------
        # Clear Cart
        # ---------------------------------------------

        if "clear cart" in message:

            self.order.clear_cart()

            reply = "🗑️ Cart cleared successfully."

            self.memory.add_bot_message(reply)

            return reply

        # ---------------------------------------------
        # Remove Item
        # ---------------------------------------------

        remove = re.search(
            r"remove (.+)",
            message
        )

        if remove:

            item = remove.group(1)

            reply = self.order.remove_item(item)

            self.memory.add_bot_message(reply)

            return reply

        # ---------------------------------------------
        # Add Item
        # ---------------------------------------------

        add = re.search(
            r"add (.+)",
            user_message,
            re.IGNORECASE
        )

        if add:

            item = add.group(1)

            reply = self.order.add_item(item)

            self.memory.add_bot_message(reply)

            return reply

        # ---------------------------------------------
        # RAG Search
        # ---------------------------------------------

        reply = self.rag.ask(user_message)

        self.memory.add_bot_message(reply)

        return reply


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    bot = CafeChatbot()

    print("=" * 60)
    print("Meeple Cafe AI Chatbot")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        message = input("\nYou : ")

        if message.lower() == "exit":
            break

        response = bot.chat(message)

        print("\nBot :")
        print(response)
