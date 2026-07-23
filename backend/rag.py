"""
=========================================================
Meeple Cafe AI Ordering Chatbot
RAG Engine
Version : 1.0
=========================================================
"""

from vector_store import VectorStore


class RAGEngine:
    """
    Retrieval Augmented Generation Engine

    Responsibilities
    ----------------
    • Search Menu
    • Search FAQ
    • Search Restaurant Information
    • Format AI Responses
    """

    def __init__(self):

        self.vector_store = VectorStore()

    # =====================================================
    # Main Search
    # =====================================================

    def ask(self, query):

        query = query.strip()

        if not query:
            return "Please enter your question."

        results = self.vector_store.search(query)

        if not results:
            return (
                "Sorry, I couldn't find anything "
                "related to your question."
            )

        return self.format_results(results)

    # =====================================================
    # Format Results
    # =====================================================

    def format_results(self, results):

        response = []

        for item in results:

            source = item["source"]
            data = item["data"]

            # ----------------------------
            # MENU
            # ----------------------------

            if source == "menu":

                text = (
                    f"🍽️ {data.get('Item_Name','')}\n"
                    f"Category : {data.get('Category','')}\n"
                    f"Type : {data.get('Type','')}\n"
                    f"Price : ₹{data.get('Price','')}\n"
                    f"{data.get('Description','')}"
                )

                response.append(text)

            # ----------------------------
            # FAQ
            # ----------------------------

            elif source == "faq":

                text = (
                    f"❓ {data.get('Question','')}\n"
                    f"✅ {data.get('Answer','')}"
                )

                response.append(text)

            # ----------------------------
            # Restaurant
            # ----------------------------

            elif source == "restaurant":

                lines = []

                for key, value in data.items():

                    lines.append(
                        f"{key} : {value}"
                    )

                response.append(
                    "🏢 Restaurant Information\n\n"
                    + "\n".join(lines)
                )

        return "\n\n" + "\n\n-----------------------------\n\n".join(response)

    # =====================================================
    # Menu Search
    # =====================================================

    def menu(self, query):

        results = self.vector_store.search_menu(query)

        if not results:
            return "No menu items found."

        return self.format_results(results)

    # =====================================================
    # FAQ Search
    # =====================================================

    def faq(self, query):

        results = self.vector_store.search_faq(query)

        if not results:
            return "No FAQ found."

        return self.format_results(results)

    # =====================================================
    # Restaurant Search
    # =====================================================

    def restaurant(self, query):

        results = self.vector_store.search_restaurant(query)

        if not results:
            return "No restaurant information found."

        return self.format_results(results)


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    rag = RAGEngine()

    print("=" * 60)
    print("Meeple Cafe RAG Engine")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        print()

        question = input("Ask > ")

        if question.lower() == "exit":
            break

        print()
        print(rag.ask(question))
