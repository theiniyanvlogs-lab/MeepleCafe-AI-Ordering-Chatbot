"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Utility Functions
Version : 3.0
=========================================================
"""

import uuid
import random
import re
from datetime import datetime


# =========================================================
# Date & Time
# =========================================================

def current_datetime():
    """
    Return current date and time.

    Example:
    2026-07-23 08:35:12
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# =========================================================
# Order ID
# =========================================================

def generate_order_id():
    """
    Generate unique order id.

    Example:
    ORD-9A73F8D2
    """

    return f"ORD-{uuid.uuid4().hex[:8].upper()}"


# =========================================================
# Session ID
# =========================================================

def generate_session_id():
    """
    Generate chat session id.
    """

    return uuid.uuid4().hex


# =========================================================
# Currency
# =========================================================

def format_price(price):
    """
    Format currency.

    Example:
    199 -> ₹199.00
    """

    try:

        return f"₹{float(price):,.2f}"

    except Exception:

        return f"₹{price}"


# =========================================================
# Clean Text
# =========================================================

def clean_text(text):
    """
    Normalize text.
    """

    if text is None:

        return ""

    text = str(text)

    text = text.strip()

    text = re.sub(r"\s+", " ", text)

    return text


# =========================================================
# Slug
# =========================================================

def slugify(text):
    """
    Convert text into slug.

    Example:
    Chicken Burger Deluxe

    becomes

    chicken-burger-deluxe
    """

    text = clean_text(text).lower()

    text = re.sub(r"[^a-z0-9 ]", "", text)

    return text.replace(" ", "-")


# =========================================================
# Similarity
# =========================================================

def normalize(text):
    """
    Normalize for comparisons.
    """

    return slugify(text)


# =========================================================
# Random Greeting
# =========================================================

def random_greeting():

    greetings = [

        "Welcome to Meeple Cafe! 👋",

        "Hello! 😊",

        "Hi there! 🍽️",

        "Good to see you!",

        "Welcome back!"

    ]

    return random.choice(greetings)


# =========================================================
# Restaurant Information
# =========================================================

def restaurant_info():

    return {

        "name": "Meeple Cafe",

        "phone": "+91-9876543210",

        "email": "info@meeplecafe.com",

        "address": "Chennai, Tamil Nadu",

        "opening_hours": "10:00 AM - 10:00 PM"

    }


# =========================================================
# API Response
# =========================================================

def success_response(data=None, message="Success"):

    return {

        "success": True,

        "message": message,

        "data": data

    }


def error_response(message="Something went wrong"):

    return {

        "success": False,

        "message": message

    }


# =========================================================
# Health
# =========================================================

def health_status():

    return {

        "status": "Healthy",

        "service": "Meeple Cafe AI Ordering Chatbot",

        "timestamp": current_datetime()

    }


# =========================================================
# Validation
# =========================================================

def is_number(value):

    try:

        float(value)

        return True

    except Exception:

        return False


def is_positive_number(value):

    try:

        return float(value) > 0

    except Exception:

        return False


# =========================================================
# Text Contains
# =========================================================

def contains(text, keywords):
    """
    Returns True if any keyword is present.

    Example:

    contains(
        "show burgers",
        ["burger","pizza"]
    )
    """

    text = clean_text(text).lower()

    return any(

        keyword.lower() in text

        for keyword in keywords

    )


# =========================================================
# Safe Integer
# =========================================================

def safe_int(value, default=0):

    try:

        return int(value)

    except Exception:

        return default


# =========================================================
# Safe Float
# =========================================================

def safe_float(value, default=0.0):

    try:

        return float(value)

    except Exception:

        return default


# =========================================================
# Banner
# =========================================================

def print_banner():

    print("=" * 60)

    print("Meeple Cafe AI Ordering Chatbot")

    print("Backend Utilities")

    print("=" * 60)


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    print_banner()

    print()

    print("Current Time :", current_datetime())

    print("Order ID     :", generate_order_id())

    print("Session ID   :", generate_session_id())

    print("Price        :", format_price(199))

    print("Slug         :", slugify("Chicken Burger Deluxe"))

    print("Greeting     :", random_greeting())

    print("Restaurant   :", restaurant_info())

    print("Health       :", health_status())
