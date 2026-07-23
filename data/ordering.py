"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Order Management System
Version : 1.0
=========================================================
"""

from database import DatabaseManager
from memory import ConversationMemory
from config import (
    GST_PERCENTAGE,
    DEFAULT_ORDER_STATUS,
)
from utils import format_price


class OrderManager:
    """
    Handles cart management and checkout.
    """

    def __init__(self):

        self.db = DatabaseManager()

        self.memory = ConversationMemory()

    # =====================================================
    # CART
    # =====================================================

    def add_item(

        self,
        session_id,
        item

    ):

        self.memory.add_to_cart(

            session_id,
            item

        )

        return f"✅ {item['Item_Name']} added to your cart."

    # -----------------------------------------------------

    def remove_item(

        self,
        session_id,
        item_name

    ):

        self.memory.remove_from_cart(

            session_id,
            item_name

        )

        return f"🗑️ {item_name} removed from your cart."

    # -----------------------------------------------------

    def clear_cart(self, session_id):

        self.memory.clear_cart(session_id)

        return "🛒 Cart cleared successfully."

    # =====================================================
    # CART DETAILS
    # =====================================================

    def get_cart(self, session_id):

        return self.memory.get_cart(session_id)

    # -----------------------------------------------------

    def cart_summary(self, session_id):

        cart = self.memory.get_cart(session_id)

        if not cart:

            return "🛒 Your cart is empty."

        response = []

        subtotal = 0

        response.append("🛒 Your Cart\n")

        for item in cart:

            qty = item["quantity"]

            price = float(item["Price"])

            total = qty * price

            subtotal += total

            response.append(

                f"• {item['Item_Name']} "
                f"x {qty} = {format_price(total)}"

            )

        gst = round(subtotal * GST_PERCENTAGE / 100, 2)

        grand_total = subtotal + gst

        response.append("")

        response.append(f"Subtotal : {format_price(subtotal)}")

        response.append(f"GST ({GST_PERCENTAGE}%) : {format_price(gst)}")

        response.append(f"Total : {format_price(grand_total)}")

        return "\n".join(response)

    # =====================================================
    # TOTALS
    # =====================================================

    def calculate_totals(self, session_id):

        subtotal = self.memory.cart_total(session_id)

        gst = round(subtotal * GST_PERCENTAGE / 100, 2)

        total = subtotal + gst

        return {

            "subtotal": subtotal,

            "gst": gst,

            "grand_total": total

        }

    # =====================================================
    # CUSTOMER DETAILS
    # =====================================================

    def set_customer(

        self,
        session_id,
        name="",
        phone="",
        address="",
        dining_type="",
        table_number=""

    ):

        self.memory.set_customer(

            session_id,

            name=name,

            phone=phone,

            address=address,

            dining_type=dining_type,

            table_number=table_number

        )

    # =====================================================
    # CHECKOUT
    # =====================================================

    def checkout(self, session_id):

        cart = self.memory.get_cart(session_id)

        if not cart:

            return "❌ Your cart is empty."

        customer = self.memory.get_customer(session_id)

        totals = self.calculate_totals(session_id)

        order_id = self.db.create_order(

            session_id=session_id,

            customer_name=customer["name"],

            phone=customer["phone"],

            dining_type=customer["dining_type"],

            table_number=customer["table_number"],

            address=customer["address"],

            total=totals["grand_total"],

            status=DEFAULT_ORDER_STATUS

        )

        for item in cart:

            self.db.add_order_item(

                order_id=order_id,

                item_name=item["Item_Name"],

                quantity=item["quantity"],

                price=item["Price"]

            )

        self.memory.clear_cart(session_id)

        return (
            f"🎉 Order placed successfully!\n\n"
            f"Order ID : #{order_id}\n"
            f"Total : {format_price(totals['grand_total'])}\n\n"
            "Thank you for choosing Meeple Cafe ❤️"
        )
