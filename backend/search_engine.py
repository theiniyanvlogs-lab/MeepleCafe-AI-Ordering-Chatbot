"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Menu Search Engine
Version : 2.0
=========================================================
"""

import os
import pandas as pd


class SearchEngine:
    """
    Menu Search Engine

    Features
    --------
    ✔ Load menu.csv
    ✔ Get complete menu
    ✔ Search by keyword
    ✔ Search by category
    ✔ Search by type
    ✔ Search by price
    ✔ Return JSON objects (FastAPI Ready)
    """

    def __init__(self):

        data_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data",
            "menu.csv",
        )

        try:

            self.menu = pd.read_csv(data_path).fillna("")

        except Exception as e:

            print("Unable to load menu.csv")
            print(e)

            self.menu = pd.DataFrame()

    # =====================================================
    # Get Complete Menu
    # =====================================================

    def get_all_menu(self):

        if self.menu.empty:
            return []

        return [self._row_to_dict(row) for _, row in self.menu.iterrows()]

    # =====================================================
    # Search
    # =====================================================

    def search(self, query: str):

        if self.menu.empty:
            return []

        query = query.lower().strip()

        df = self.menu.copy()

        # ------------------------------------
        # Price Search
        # ------------------------------------

        if "under" in query or "below" in query or "less" in query:

            words = query.split()

            for word in words:

                if word.isdigit():

                    price = int(word)

                    result = df[df["Price"] <= price]

                    return [
                        self._row_to_dict(row)
                        for _, row in result.iterrows()
                    ]

        # ------------------------------------
        # General Search
        # ------------------------------------

        result = df[
            df["Item_Name"].str.lower().str.contains(query, na=False)
            | df["Category"].str.lower().str.contains(query, na=False)
            | df["Sub_Category"].str.lower().str.contains(query, na=False)
            | df["Description"].str.lower().str.contains(query, na=False)
            | df["Keywords"].str.lower().str.contains(query, na=False)
            | df["Type"].str.lower().str.contains(query, na=False)
        ]

        return [
            self._row_to_dict(row)
            for _, row in result.iterrows()
        ]

    # =====================================================
    # Veg / Non-Veg
    # =====================================================

    def search_type(self, food_type: str):

        if self.menu.empty:
            return []

        result = self.menu[
            self.menu["Type"].str.lower() == food_type.lower()
        ]

        return [
            self._row_to_dict(row)
            for _, row in result.iterrows()
        ]

    # =====================================================
    # Category
    # =====================================================

    def search_category(self, category: str):

        if self.menu.empty:
            return []

        result = self.menu[
            self.menu["Category"]
            .str.lower()
            .str.contains(category.lower(), na=False)
        ]

        return [
            self._row_to_dict(row)
            for _, row in result.iterrows()
        ]

    # =====================================================
    # Price
    # =====================================================

    def search_price(self, max_price: int):

        if self.menu.empty:
            return []

        result = self.menu[
            self.menu["Price"] <= max_price
        ]

        return [
            self._row_to_dict(row)
            for _, row in result.iterrows()
        ]

    # =====================================================
    # Convert Row to Dictionary
    # =====================================================

    def _row_to_dict(self, row):

        return {
            "id": int(row["Item_ID"]),
            "name": row["Item_Name"],
            "category": row["Category"],
            "sub_category": row["Sub_Category"],
            "type": row["Type"],
            "price": float(row["Price"]),
            "description": row["Description"],
            "keywords": row["Keywords"],
            "available": row["Available"],
        }
