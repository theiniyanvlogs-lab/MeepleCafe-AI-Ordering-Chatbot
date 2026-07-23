"""
=========================================================
Meeple Cafe AI Ordering Chatbot
FAISS Vector Store
Version : 3.1 (Lazy Loading)
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
    ✔ Lazy Loading
    ✔ FAISS Search
    ✔ SentenceTransformer Embeddings
    ✔ Metadata Lookup
    """

    def __init__(self):

        self.index = None
        self.metadata = []
        self.model = None
        self.loaded = False

    # =====================================================
    # Lazy Load
    # =====================================================

    def ensure_loaded(self):

        if self.loaded:
            return

        print("=" * 60)
        print("Loading Vector Store...")
        print("=" * 60)

        self._load_model()
        self._load_index()
        self._load_metadata()

        self.loaded = True

        print("Vector Store Ready")
        print("=" * 60)

    # =====================================================
    # Load Model
    # =====================================================

    def _load_model(self):

        print("Loading SentenceTransformer...")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

        print("SentenceTransformer Loaded")

    # =====================================================
    # Load FAISS
    # =====================================================

    def _load_index(self):

        print("Loading FAISS Index...")

        if not os.path.exists(FAISS_INDEX):
            raise FileNotFoundError(
                f"FAISS index not found:\n{FAISS_INDEX}"
            )

        self.index = faiss.read_index(FAISS_INDEX)

        print(f"Loaded {self.index.ntotal} vectors")

    # =====================================================
    # Load Metadata
    # =====================================================

    def _load_metadata(self):

        print("Loading Metadata...")

        if not os.path.exists(FAISS_METADATA):
            raise FileNotFoundError(
                f"Metadata not found:\n{FAISS_METADATA}"
            )

        with open(FAISS_METADATA, "rb") as f:
            self.metadata = pickle.load(f)

        print(f"Loaded {len(self.metadata)} metadata records")

    # =====================================================
    # Encode
    # =====================================================

    def encode(self, text):

        self.ensure_loaded()

        embedding = self.model.encode(
            [text],
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.astype(np.float32)

    # =====================================================
    # Search
    # =====================================================

    def search(self, query, top_k=TOP_K):

        self.ensure_loaded()

        embedding = self.encode(query)

        distances, indices = self.index.search(
            embedding,
            top_k
        )

        results = []

        for score, idx in zip(distances[0], indices[0]):

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

    def best_match(self, query):

        results = self.search(query, 1)

        return results[0] if results else None

    # =====================================================
    # Size
    # =====================================================

    def size(self):

        self.ensure_loaded()

        return self.index.ntotal

    # =====================================================
    # Info
    # =====================================================

    def info(self):

        return {
            "loaded": self.loaded,
            "embedding_model": EMBEDDING_MODEL,
            "vectors": self.index.ntotal if self.loaded else 0,
            "metadata_records": len(self.metadata),
            "top_k": TOP_K,
        }


# =========================================================
# Singleton
# =========================================================

vector_store = VectorStore()
