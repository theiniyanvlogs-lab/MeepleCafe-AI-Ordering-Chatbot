"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Configuration File
Version : 1.0
=========================================================
"""

import os

# =========================================================
# PROJECT INFORMATION
# =========================================================

PROJECT_NAME = "Meeple Cafe AI Ordering Chatbot"
VERSION = "1.0.0"

# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..")
)

# =========================================================
# DATA PATHS
# =========================================================

DATA_DIR = os.path.join(ROOT_DIR, "data")

MENU_FILE = os.path.join(DATA_DIR, "menu.csv")

FAQ_FILE = os.path.join(DATA_DIR, "faq.csv")

RESTAURANT_FILE = os.path.join(DATA_DIR, "restaurant.csv")

DATABASE_FILE = os.path.join(DATA_DIR, "restaurant.db")

# =========================================================
# VECTOR DATABASE
# =========================================================

VECTOR_DIR = os.path.join(ROOT_DIR, "vector_db")

FAISS_INDEX = os.path.join(
    VECTOR_DIR,
    "menu.index"
)

METADATA_FILE = os.path.join(
    VECTOR_DIR,
    "metadata.pkl"
)

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

TOP_K_RESULTS = 5

SIMILARITY_THRESHOLD = 0.50

# =========================================================
# CHATBOT SETTINGS
# =========================================================

DEFAULT_SESSION = "guest"

MAX_CHAT_HISTORY = 20

WELCOME_MESSAGE = """
👋 Welcome to Meeple Cafe!

I can help you with:

🍔 Burgers
🍕 Pizza
🍝 Pasta
☕ Coffee
🥤 Shakes
🍟 Snacks
🧇 Desserts

You can also:

• Search Menu
• View Prices
• Place Orders
• View Cart
• Checkout

How can I help you today?
"""

# =========================================================
# ORDER SETTINGS
# =========================================================

DEFAULT_ORDER_STATUS = "Pending"

DEFAULT_QUANTITY = 1

GST_PERCENTAGE = 5

CURRENCY = "₹"

# =========================================================
# RESTAURANT SETTINGS
# =========================================================

RESTAURANT_NAME = "Meeple Cafe"

OPEN_TIME = "10:00 AM"

CLOSE_TIME = "11:00 PM"

HAPPY_HOURS = "3:00 PM - 6:00 PM"

# =========================================================
# API SETTINGS
# =========================================================

HOST = "0.0.0.0"

PORT = 8000

DEBUG = True

# =========================================================
# FRONTEND
# =========================================================

ALLOWED_ORIGINS = [
    "*"
]

# =========================================================
# SEARCH SETTINGS
# =========================================================

SEARCHABLE_COLUMNS = [
    "Item_Name",
    "Category",
    "Sub_Category",
    "Description",
    "Keywords"
]

# =========================================================
# SUPPORTED CATEGORIES
# =========================================================

MENU_CATEGORIES = [

    "Burger",

    "Pizza",

    "Pasta",

    "Shakes & Smoothies",

    "Frappe",

    "Hot Beverages",

    "Iced Coffee",

    "Refreshers",

    "Desserts",

    "Small Plates",

    "Sandwiches & Wraps"

]

# =========================================================
# END
# =========================================================
