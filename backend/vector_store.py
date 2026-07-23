"""
=========================================================
Meeple Cafe AI Ordering Chatbot
FAISS Vector Store
Version : 1.0
=========================================================
"""

import os
import pickle

import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from config import (
    FAISS_INDEX,
    METADATA_FILE,
    EMBEDDING_MODEL,
    TOP_K_RESULTS
)


class VectorStore:
    """
    FAISS Vector Search Engine
    """

    def __init__(self):

        if not os.path.exists(FAISS_INDEX):
            raise FileNotFoundError(
                f"FAISS index not found:\n{FAISS_INDEX}"
            )

        if not os.path.exists(METADATA_FILE):
            raise FileNotFoundError(
                f"Metadata file not found:\n{METADATA_FILE}"
            )

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print("Loading FAISS index...")

        self.index = faiss.read_index(
            FAISS_INDEX
        )

        print("Loading metadata...")

        with open(METADATA_FILE, "rb") as f:
            self.metadata = pickle.load(f)

        print("=" * 50)
        print("Vector Store Loaded Successfully")
        print(f"Documents : {len(self.metadata)}")
        print("=" * 50)

    # =====================================================
    # Encode Query
    # =====================================================

    def encode(self, query):

        embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        return embedding.astype("float32")

    # =====================================================
    # Search
    # =====================================================

    def search(

        self,
        query,
        top_k=TOP_K_RESULTS

    ):

        embedding = self.encode(query)

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        for distance, idx in zip(
            distances[0],
            indices[0]
        ):

            if idx == -1:
                continue

            item = self.metadata[idx]

            results.append({

                "score": float(distance),

                "source": item["source"],

                "data": item["data"]

            })

        return results

    # =====================================================
    # Search by Source
    # =====================================================

    def search_source(

        self,
        query,
        source,
        top_k=TOP_K_RESULTS

    ):

        results = self.search(query, top_k * 3)

        filtered = []

        for item in results:

            if item["source"] == source:

                filtered.append(item)

        return filtered[:top_k]

    # =====================================================
    # Menu Search
    # =====================================================

    def search_menu(

        self,
        query,
        top_k=TOP_K_RESULTS

    ):

        return self.search_source(
            query,
            "menu",
            top_k
        )

    # =====================================================
    # FAQ Search
    # =====================================================

    def search_faq(

        self,
        query,
        top_k=TOP_K_RESULTS

    ):

        return self.search_source(
            query,
            "faq",
            top_k
        )

    # =====================================================
    # Restaurant Search
    # =====================================================

    def search_restaurant(

        self,
        query,
        top_k=TOP_K_RESULTS

    ):

        return self.search_source(
            query,
            "restaurant",
            top_k
        )


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    store = VectorStore()

    while True:

        print()

        query = input("Ask > ")

        if query.lower() == "exit":
            break

        results = store.search(query)

        print()

        for i, item in enumerate(results, 1):

            print("=" * 50)

            print(f"Result {i}")

            print("Source :", item["source"])

            print("Distance :", round(item["score"], 4))

            print(item["data"])
