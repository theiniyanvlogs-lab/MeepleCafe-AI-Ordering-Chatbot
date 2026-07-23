"""
=========================================================
Meeple Cafe AI Ordering Chatbot
RAG Engine
Version : 3.0
=========================================================
"""

try:
    from backend.vector_store import vector_store
    from backend.search_engine import SearchEngine
    from backend.config import TOP_K
except ImportError:
    from vector_store import vector_store
    from search_engine import SearchEngine
    from config import TOP_K


class RAGEngine:
    """
    Retrieval Augmented Generation Engine

    Features
    --------
    ✔ Semantic Search (FAISS)
    ✔ Keyword Search (CSV)
    ✔ Menu Search
    ✔ FAQ Search
    ✔ Restaurant Search
    ✔ Context Builder
    ✔ AI Response Formatter
    """

    def __init__(self):

        self.vector_store = vector_store
        self.search_engine = SearchEngine()

    # =====================================================
    # Main Search
    # =====================================================

    def ask(self, query):

        return self.answer(query)

    # =====================================================
    # AI Answer
    # =====================================================

    def answer(self, query):

        query = query.strip()

        if not query:

            return "Please enter your question."

        # --------------------------------------------
        # Semantic Search
        # --------------------------------------------

        results = self.vector_store.search(
            query=query,
            top_k=TOP_K
        )

        # --------------------------------------------
        # Fallback Search
        # --------------------------------------------

        if not results:

            results = self.search_engine.search(query)

            if results:

                return self.format_menu(results)

            return (
                "Sorry, I couldn't find anything "
                "related to your question."
            )

        return self.format_results(results)

    # =====================================================
    # Build Context
    # =====================================================

    def build_context(self, query):

        results = self.vector_store.search(
            query=query,
            top_k=TOP_K
        )

        if not results:

            return ""

        lines = []

        for item in results:

            source = item.get("source", "")

            data = item.get("data", {})

            if source == "menu":

                lines.append(

                    f"{data.get('Item_Name','')} | "

                    f"{data.get('Category','')} | "

                    f"{data.get('Type','')} | "

                    f"₹{data.get('Price','')}"

                )

        return "\n".join(lines)

    # =====================================================
    # Format Results
    # =====================================================

    def format_results(self, results):

        response = []

        for item in results:

            source = item.get("source", "")

            data = item.get("data", {})

            # ----------------------------------------
            # Menu
            # ----------------------------------------

            if source == "menu":

                response.append(

                    f"🍽️ {data.get('Item_Name','Unknown')}\n"

                    f"📂 Category : {data.get('Category','-')}\n"

                    f"🥗 Type : {data.get('Type','-')}\n"

                    f"💰 Price : ₹{data.get('Price','-')}\n"

                    f"📝 {data.get('Description','')}"

                )

            # ----------------------------------------
            # FAQ
            # ----------------------------------------

            elif source == "faq":

                response.append(

                    f"❓ {data.get('Question','')}\n\n"

                    f"✅ {data.get('Answer','')}"

                )

            # ----------------------------------------
            # Restaurant
            # ----------------------------------------

            elif source == "restaurant":

                info = []

                for key, value in data.items():

                    info.append(f"{key} : {value}")

                response.append(

                    "🏢 Restaurant Information\n\n"

                    + "\n".join(info)

                )

        if not response:

            return "No matching information found."

        return "\n\n" + "\n\n----------------------------------------\n\n".join(response)

    # =====================================================
    # Format Menu (Fallback Search)
    # =====================================================

    def format_menu(self, results):

        response = []

        for item in results:

            response.append(

                f"🍽️ {item.get('name','')}\n"

                f"📂 {item.get('category','')}\n"

                f"🥗 {item.get('type','')}\n"

                f"💰 ₹{item.get('price','')}\n"

                f"{item.get('description','')}"

            )

        return "\n\n".join(response)

    # =====================================================
    # Menu Search
    # =====================================================

    def menu(self, query):

        results = self.search_engine.search(query)

        if not results:

            return "No menu items found."

        return self.format_menu(results)

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

    # =====================================================
    # Retrieve Raw Results
    # =====================================================

    def retrieve(self, query):

        return self.vector_store.search(
            query=query,
            top_k=TOP_K
        )

    # =====================================================
    # Health Check
    # =====================================================

    def info(self):

        return {

            "vector_store": self.vector_store.info(),

            "top_k": TOP_K,

            "status": "Ready"

        }


# =========================================================
# Singleton
# =========================================================

rag_engine = RAGEngine()


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Meeple Cafe AI Ordering Chatbot")
    print("RAG Engine Version 3.0")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        query = input("\nAsk > ").strip()

        if query.lower() == "exit":

            break

        print()

        print(rag_engine.answer(query))
