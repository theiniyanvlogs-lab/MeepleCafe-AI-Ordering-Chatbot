"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Build FAISS Vector Database
Version : 1.0
=========================================================
"""

import os
import pickle

import faiss
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer

from config import (
    MENU_FILE,
    FAQ_FILE,
    RESTAURANT_FILE,
    VECTOR_DIR,
    FAISS_INDEX,
    METADATA_FILE,
    EMBEDDING_MODEL,
)


class VectorDatabaseBuilder:
    """
    Builds the FAISS vector database from CSV files.
    """

    def __init__(self):

        self.model = SentenceTransformer(EMBEDDING_MODEL)

        self.documents = []

        self.metadata = []

    # =====================================================
    # MENU
    # =====================================================

    def load_menu(self):

        if not os.path.exists(MENU_FILE):
            print("Menu file not found.")
            return

        df = pd.read_csv(MENU_FILE).fillna("")

        for _, row in df.iterrows():

            text = (
                f"Menu Item: {row['Item_Name']}. "
                f"Category: {row['Category']}. "
                f"Sub Category: {row['Sub_Category']}. "
                f"Type: {row['Type']}. "
                f"Price: ₹{row['Price']}. "
                f"Description: {row['Description']}. "
                f"Keywords: {row['Keywords']}."
            )

            self.documents.append(text)

            self.metadata.append({
                "source": "menu",
                "data": row.to_dict()
            })

    # =====================================================
    # FAQ
    # =====================================================

    def load_faq(self):

        if not os.path.exists(FAQ_FILE):
            print("FAQ file not found.")
            return

        df = pd.read_csv(FAQ_FILE).fillna("")

        for _, row in df.iterrows():

            text = (
                f"Question: {row['Question']}. "
                f"Answer: {row['Answer']}. "
                f"Category: {row['Category']}. "
                f"Keywords: {row['Keywords']}."
            )

            self.documents.append(text)

            self.metadata.append({
                "source": "faq",
                "data": row.to_dict()
            })

    # =====================================================
    # RESTAURANT
    # =====================================================

    def load_restaurant(self):

        if not os.path.exists(RESTAURANT_FILE):
            print("Restaurant file not found.")
            return

        df = pd.read_csv(RESTAURANT_FILE).fillna("")

        for _, row in df.iterrows():

            text = f"{row['Field']}: {row['Value']}"

            self.documents.append(text)

            self.metadata.append({
                "source": "restaurant",
                "data": row.to_dict()
            })

    # =====================================================
    # BUILD
    # =====================================================

    def build(self):

        print("=" * 50)
        print("Loading data...")
        print("=" * 50)

        self.load_menu()
        self.load_faq()
        self.load_restaurant()

        print(f"Total Documents : {len(self.documents)}")

        if len(self.documents) == 0:
            print("No documents found.")
            return

        print("\nGenerating embeddings...")

        embeddings = self.model.encode(
            self.documents,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        embeddings = embeddings.astype("float32")

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(embeddings)

        os.makedirs(VECTOR_DIR, exist_ok=True)

        faiss.write_index(index, FAISS_INDEX)

        with open(METADATA_FILE, "wb") as f:
            pickle.dump(self.metadata, f)

        print("\nVector database created successfully!")
        print(f"Documents : {len(self.documents)}")
        print(f"Dimension : {dimension}")
        print(f"Index File : {FAISS_INDEX}")
        print(f"Metadata File : {METADATA_FILE}")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    builder = VectorDatabaseBuilder()

    builder.build()
