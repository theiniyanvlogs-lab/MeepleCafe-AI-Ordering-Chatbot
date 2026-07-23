"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Utility Functions
Version : 1.0
=========================================================
"""

import re
from datetime import datetime

from config import CURRENCY


# =========================================================
# TEXT UTILITIES
# =========================================================

def clean_text(text: str) -> str:
    """
    Clean and normalize text.
    """

    if text is None:
        return ""

    text = str(text)

    text = text.strip()

    text = re.sub(r"\s+", " ", text)

    return text


def normalize_text(text: str) -> str:
    """
    Lowercase + clean text.
    """

    return clean_text(text).lower()


# =========================================================
# GREETING
# =========================================================

def is_greeting(message: str) -> bool:

    greetings = [

        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"

    ]

    return normalize_text(message) in greetings


# =========================================================
# PRICE EXTRACTION
# =========================================================

def extract_price(query: str):

    """
    Examples

    below 200

    under 300

    less than 150

    250
    """

    numbers = re.findall(r"\d+", query)

    if numbers:

        return int(numbers[0])

    return None


# =========================================================
# CURRENCY
# =========================================================

def format_price(price):

    try:

        return f"{CURRENCY}{float(price):.0f}"

    except:

        return f"{CURRENCY}0"


# =========================================================
# MENU CARD
# =========================================================

def format_menu_item(item: dict):

    return (
        f"🍽️ {item['Item_Name']}\n"
        f"📂 {item['Category']}\n"
        f"🥗 {item['Type']}\n"
        f"💰 {format_price(item['Price'])}\n"
        f"📝 {item['Description']}"
    )


# =========================================================
# MULTIPLE MENU ITEMS
# =========================================================

def format_menu_list(items):

    if len(items) == 0:

        return "No menu items found."

    response = []

    for item in items:

        response.append(format_menu_item(item))

    return "\n\n-------------------------\n\n".join(response)


# =========================================================
# ORDER ID
# =========================================================

def generate_order_number():

    now = datetime.now()

    return now.strftime("MC%Y%m%d%H%M%S")


# =========================================================
# DATE TIME
# =========================================================

def current_datetime():

    return datetime.now().strftime(
        "%d-%m-%Y %I:%M:%S %p"
    )


# =========================================================
# RESPONSE
# =========================================================

def success(message):

    return {

        "status": "success",

        "message": message

    }


def error(message):

    return {

        "status": "error",

        "message": message

    }


# =========================================================
# YES / NO
# =========================================================

def is_yes(text):

    words = [

        "yes",

        "yeah",

        "ok",

        "okay",

        "sure"

    ]

    return normalize_text(text) in words


def is_no(text):

    words = [

        "no",

        "nope",

        "cancel"

    ]

    return normalize_text(text) in words


# =========================================================
# END
# =========================================================
