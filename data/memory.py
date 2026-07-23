"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Conversation Memory Manager
Version : 1.0
=========================================================
"""

from copy import deepcopy

from config import (
    DEFAULT_SESSION,
    MAX_CHAT_HISTORY,
)


class ConversationMemory:
    """
    Manages temporary conversation memory for each user.
    """

    def __init__(self):

        self.sessions = {}

    # =====================================================
    # INTERNAL
    # =====================================================

    def _create_session(self):

        return {

            "history": [],

            "cart": [],

            "last_results": [],

            "customer": {

                "name": "",

                "phone": "",

                "address": "",

                "dining_type": "",

                "table_number": ""

            }

        }

    def _ensure(self, session_id):

        if not session_id:

            session_id = DEFAULT_SESSION

        if session_id not in self.sessions:

            self.sessions[session_id] = self._create_session()

        return self.sessions[session_id]

    # =====================================================
    # CHAT HISTORY
    # =====================================================

    def add_message(

        self,
        session_id,
        role,
        message

    ):

        session = self._ensure(session_id)

        session["history"].append({

            "role": role,

            "message": message

        })

        if len(session["history"]) > MAX_CHAT_HISTORY:

            session["history"] = session["history"][-MAX_CHAT_HISTORY:]

    def get_history(self, session_id):

        return self._ensure(session_id)["history"]

    def clear_history(self, session_id):

        self._ensure(session_id)["history"] = []

    # =====================================================
    # LAST SEARCH RESULTS
    # =====================================================

    def set_last_results(

        self,
        session_id,
        results

    ):

        self._ensure(session_id)["last_results"] = deepcopy(results)

    def get_last_results(self, session_id):

        return self._ensure(session_id)["last_results"]

    # =====================================================
    # CART
    # =====================================================

    def add_to_cart(

        self,
        session_id,
        item

    ):

        session = self._ensure(session_id)

        cart = session["cart"]

        for cart_item in cart:

            if cart_item["Item_Name"] == item["Item_Name"]:

                cart_item["quantity"] += 1

                return

        new_item = deepcopy(item)

        new_item["quantity"] = 1

        cart.append(new_item)

    def remove_from_cart(

        self,
        session_id,
        item_name

    ):

        session = self._ensure(session_id)

        cart = session["cart"]

        session["cart"] = [

            item

            for item in cart

            if item["Item_Name"].lower() != item_name.lower()

        ]

    def clear_cart(self, session_id):

        self._ensure(session_id)["cart"] = []

    def get_cart(self, session_id):

        return self._ensure(session_id)["cart"]

    def cart_total(self, session_id):

        total = 0

        for item in self.get_cart(session_id):

            total += float(item["Price"]) * item["quantity"]

        return round(total, 2)

    # =====================================================
    # CUSTOMER DETAILS
    # =====================================================

    def set_customer(

        self,
        session_id,
        **kwargs

    ):

        customer = self._ensure(session_id)["customer"]

        for key, value in kwargs.items():

            if key in customer:

                customer[key] = value

    def get_customer(self, session_id):

        return self._ensure(session_id)["customer"]

    # =====================================================
    # SESSION
    # =====================================================

    def reset_session(self, session_id):

        self.sessions[session_id] = self._create_session()

    def session_exists(self, session_id):

        return session_id in self.sessions

    def all_sessions(self):

        return list(self.sessions.keys())
