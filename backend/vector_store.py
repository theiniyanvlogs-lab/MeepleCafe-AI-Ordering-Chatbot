"""
=========================================================
Meeple Cafe AI Ordering Chatbot
FAISS Vector Store
Version : 3.0
=========================================================
"""

import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

try:
    from backend.config import (
        FAISS_INDEX,
        FAISS_METADATA,
        EMBEDDING_MODEL,
        TOP_K,
    )
except ImportError:
    from config import (
        FAISS_INDEX,
        FAISS_METADATA,
        EMBEDDING_MODEL,
        TOP_K,
    )


class VectorStore:
    """
    FAISS Vector Store

    Features
    --------
    ✔ Load FAISS index
    ✔ Load metadata
    ✔ Load embedding model
    ✔ Semantic similarity search
    ✔ Return top-k menu chunks
    """

    def __init__(self):

        self.index = None
        self.metadata = []
        self.model = None

        self.load()

    # =====================================================
    # Load Everything
    # =====================================================

    def load(self):

        self._load_model()
        self._load_index()
        self._load_metadata()

    # =====================================================
    # Load Embedding Model
    # =====================================================

    def _load_model(self):

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    # =====================================================
    # Load FAISS Index
    # =====================================================

    def _load_index(self):

        if not os.path.exists(FAISS_INDEX):

            raise FileNotFoundError(
                f"FAISS index not found:\n{FAISS_INDEX}"
            )

        self.index = faiss.read_index(
            str(FAISS_INDEX)
        )

    # =====================================================
    # Load Metadata
    # =====================================================

    def _load_metadata(self):

        if not os.path.exists(FAISS_METADATA):

            raise FileNotFoundError(
                f"Metadata file not found:\n{FAISS_METADATA}"
            )

        with open(FAISS_METADATA, "rb") as f:

            self.metadata = pickle.load(f)

    # =====================================================
    # Encode Query
    # =====================================================

    def encode(self, text: str):

        embedding = self.model.encode(
            [text],
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.astype(np.float32)

    # =====================================================
    # Search
    # =====================================================

    def search(
        self,
        query: str,
        top_k: int = TOP_K
    ):

        if self.index is None:

            return []

        embedding = self.encode(query)

        distances, indices = self.index.search(
            embedding,
            top_k,
        )

        results = []

        for score, idx in zip(
            distances[0],
            indices[0],
        ):

            if idx < 0:
                continue

            if idx >= len(self.metadata):
                continue

            item = self.metadata[idx].copy()

            item["score"] = float(score)

            results.append(item)

        return results

    # =====================================================
    # Best Match
    # =====================================================

    def best_match(self, query: str):

        results = self.search(query, 1)

        if results:

            return results[0]

        return None

    # =====================================================
    # Number of Vectors
    # =====================================================

    def size(self):

        if self.index is None:

            return 0

        return self.index.ntotal

    # =====================================================
    # Information
    # =====================================================

    def info(self):

        return {

            "embedding_model": EMBEDDING_MODEL,

            "vectors": self.size(),

            "metadata_records": len(self.metadata),

            "top_k": TOP_K,

        }


# =========================================================
# Singleton
# =========================================================

vector_store = VectorStore()
