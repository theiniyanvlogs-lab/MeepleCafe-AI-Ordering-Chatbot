"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Configuration
Version : 3.0
=========================================================
"""

import os
from pathlib import Path

# =========================================================
# Project Directories
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

BACKEND_DIR = BASE_DIR / "backend"

DATA_DIR = BASE_DIR / "data"

VECTOR_DB_DIR = BASE_DIR / "vector_db"

MODEL_DIR = BASE_DIR / "models"

LOG_DIR = BASE_DIR / "logs"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
VECTOR_DB_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# =========================================================
# Data Files
# =========================================================

MENU_CSV = DATA_DIR / "menu.csv"

ORDERS_DB = DATA_DIR / "orders.db"

# =========================================================
# Vector Database
# =========================================================

FAISS_INDEX = VECTOR_DB_DIR / "menu.index"

FAISS_METADATA = VECTOR_DB_DIR / "metadata.pkl"

# =========================================================
# Embedding Model
# =========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# =========================================================
# RAG Settings
# =========================================================

TOP_K = 5

SIMILARITY_THRESHOLD = 0.30

MAX_RESULTS = 10

# =========================================================
# Chatbot
# =========================================================

BOT_NAME = "Meeple Cafe AI"

WELCOME_MESSAGE = (
    "👋 Welcome to Meeple Cafe!\n"
    "How can I help you today?"
)

DEFAULT_FALLBACK = (
    "Sorry, I couldn't find that on our menu. "
    "Please try another search."
)

# =========================================================
# Restaurant Information
# =========================================================

RESTAURANT_NAME = "Meeple Cafe"

RESTAURANT_ADDRESS = "Chennai, Tamil Nadu"

RESTAURANT_PHONE = "+91 9876543210"

RESTAURANT_EMAIL = "support@meeplecafe.com"

OPENING_HOURS = "09:00 AM - 10:00 PM"

# =========================================================
# Order
# =========================================================

DEFAULT_ORDER_STATUS = "Preparing"

SUPPORTED_PAYMENTS = [
    "Cash",
    "UPI",
    "Card"
]

# =========================================================
# FastAPI
# =========================================================

API_TITLE = "Meeple Cafe AI Ordering Chatbot"

API_VERSION = "3.0.0"

API_DESCRIPTION = "AI Powered Restaurant Ordering Assistant"

HOST = "0.0.0.0"

PORT = 8000

DEBUG = True

# =========================================================
# CORS
# =========================================================

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# =========================================================
# Logging
# =========================================================

LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "application.log"

# =========================================================
# Helper Functions
# =========================================================

def get_database_path() -> str:
    return str(ORDERS_DB)


def get_menu_path() -> str:
    return str(MENU_CSV)


def get_faiss_index_path() -> str:
    return str(FAISS_INDEX)


def get_metadata_path() -> str:
    return str(FAISS_METADATA)
