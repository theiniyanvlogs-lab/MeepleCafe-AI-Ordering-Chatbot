"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Menu Search Engine
Version : 1.0
=========================================================
"""

import os
import pandas as pd


class MenuSearchEngine:
    """
    Menu Search Engine

    Responsibilities
    ----------------
    1. Load Menu CSV
    2. Search by Category
    3. Search by Item Name
    4. Search by Price
    5. Search by Veg / Non-Veg
    """

    def __init__(self):

        data_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data",
            "menu.csv"
        )

        try:
            self.menu = pd.read_csv(data_path).fillna("")
        except Exception:
            self.menu = pd.DataFrame()

    # --------------------------------------------------
    # Main Search
    # --------------------------------------------------

    def search(self, query: str):

        if self.menu.empty:
            return "Menu database is empty."

        query = query.lower().strip()

        # ----------------------------
        # Category Search
        # ----------------------------

        categories = [
            "burger",
            "pizza",
            "pasta",
            "sandwich",
            "coffee",
            "shake",
            "snack",
            "dessert",
            "beverage",
            "maggi"
        ]

        for category in categories:

            if category in query:

                return self.search_category(category)

        # ----------------------------
        # Veg Search
        # ----------------------------

        if "veg" in query:

            return self.search_type("Veg")

        if "non veg" in query or "nonveg" in query:

            return self.search_type("Non Veg")

        # ----------------------------
        # Price Search
        # Example:
        # below 200
        # under 150
        # ----------------------------

        words = query.split()

        for i, word in enumerate(words):

            if word in ["below", "under", "less"]:

                if i + 1 < len(words):

                    try:
                        price = int(words[i + 1])

                        return self.search_price(price)

                    except ValueError:
                        pass

        # ----------------------------
        # Item Search
        # ----------------------------

        return self.search_item(query)

    # --------------------------------------------------
    # Category Search
    # --------------------------------------------------

    def search_category(self, category):

        result = self.menu[
            self.menu["Category"]
            .str.lower()
            .str.contains(category)
        ]

        if result.empty:
            return "No items found."

        return self.format_result(result)

    # --------------------------------------------------
    # Item Search
    # --------------------------------------------------

    def search_item(self, keyword):

        result = self.menu[
            self.menu["Item_Name"]
            .str.lower()
            .str.contains(keyword)
        ]

        if result.empty:
            return "No matching item found."

        return self.format_result(result)

    # --------------------------------------------------
    # Veg / Non-Veg
    # --------------------------------------------------

    def search_type(self, food_type):

        result = self.menu[
            self.menu["Type"]
            .str.lower() ==
            food_type.lower()
        ]

        if result.empty:
            return "No items found."

        return self.format_result(result)

    # --------------------------------------------------
    # Price Search
    # --------------------------------------------------

    def search_price(self, price):

        result = self.menu[
            self.menu["Price"] <= price
        ]

        if result.empty:
            return "No items found."

        return self.format_result(result)

    # --------------------------------------------------
    # Format Output
    # --------------------------------------------------

    def format_result(self, dataframe):

        response = []

        for _, row in dataframe.iterrows():

            response.append(
                f"🍽️ {row['Item_Name']}\n"
                f"📂 {row['Category']}\n"
                f"🥗 {row['Type']}\n"
                f"💰 ₹{row['Price']}\n"
            )

        return "\n".join(response)
