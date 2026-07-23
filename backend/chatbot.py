"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Main Chatbot Controller
Version : 2.0
=========================================================
"""

import re

try:
    from backend.rag import RAGEngine
    from backend.ordering import OrderManager
    from backend.memory import ConversationMemory
except ImportError:
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

    def _reply(self, text: str):
        try:
            self.memory.add_bot_message(text)
        except Exception:
            pass
        return text

    def chat(self, user_message: str):

        try:
            user_message = user_message.strip()

            if not user_message:
                return "Please enter your message."

            try:
                self.memory.add_user_message(user_message)
            except Exception:
                pass

            message = user_message.lower()

            greetings = [
                "hi", "hello", "hey",
                "good morning", "good afternoon",
                "good evening"
            ]

            if any(g == message or message.startswith(g) for g in greetings):
                return self._reply(
                    "👋 Welcome to Meeple Cafe!\n\n"
                    "How may I help you today?\n\n"
                    "Examples:\n"
                    "• Show burgers\n"
                    "• Pizza under ₹300\n"
                    "• Do you have desserts?\n"
                    "• Add Classic Vegetable Stack\n"
                    "• View cart\n"
                    "• Checkout"
                )

            if message in ("view cart", "cart"):
                return self._reply(self.order.view_cart())

            if message == "checkout":
                return self._reply(self.order.checkout())

            if message == "clear cart":
                self.order.clear_cart()
                return self._reply("🗑️ Cart cleared successfully.")

            remove = re.search(r"remove\s+(.+)", message, re.I)
            if remove:
                return self._reply(
                    self.order.remove_item(remove.group(1).strip())
                )

            add = re.search(r"add\s+(.+)", user_message, re.I)
            if add:
                return self._reply(
                    self.order.add_item(add.group(1).strip())
                )

            return self._reply(self.rag.ask(user_message))

        except Exception as e:
            return f"⚠️ Sorry, an unexpected error occurred.\n\n{e}"


if __name__ == "__main__":

    bot = CafeChatbot()

    print("=" * 60)
    print("Meeple Cafe AI Chatbot")
    print("=" * 60)
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You : ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        print("\nBot :")
        print(bot.chat(query))
        print()
