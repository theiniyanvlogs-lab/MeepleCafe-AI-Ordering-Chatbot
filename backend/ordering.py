"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Order Manager
Version : 3.0
=========================================================
"""

import os
import pandas as pd

try:
    from backend.database import db
except ImportError:
    from database import db


class OrderManager:

    def __init__(self):

        self.menu_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data",
            "menu.csv"
        )

        self.menu = self._load_menu()

    # =====================================================
    # Load Menu
    # =====================================================

    def _load_menu(self):

        try:

            df = pd.read_csv(self.menu_path).fillna("")

            df["Item_ID"] = df["Item_ID"].astype(int)

            return df

        except Exception as e:

            print("Unable to load menu.csv")

            print(e)

            return pd.DataFrame()

    # =====================================================
    # Reload Menu
    # =====================================================

    def reload_menu(self):

        self.menu = self._load_menu()

    # =====================================================
    # Place Order
    # =====================================================

    def place_order(
        self,
        customer_name,
        phone,
        email,
        address,
        payment_method,
        items
    ):

        if self.menu.empty:
            raise Exception("Menu database is empty.")

        if len(items) == 0:
            raise Exception("Cart is empty.")

        total = 0

        order_items = []

        for item in items:

            quantity = int(item["quantity"])

            if quantity <= 0:
                continue

            result = self.menu[
                self.menu["Item_ID"] == int(item["id"])
            ]

            if result.empty:
                continue

            row = result.iloc[0]

            if str(row["Available"]).lower() != "yes":
                continue

            price = float(row["Price"])

            subtotal = price * quantity

            total += subtotal

            order_items.append({

                "item_id": int(row["Item_ID"]),

                "item_name": row["Item_Name"],

                "quantity": quantity,

                "price": price,

                "subtotal": subtotal

            })

        if len(order_items) == 0:
            raise Exception("No valid items available for ordering.")

        with db.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO orders(

                    customer_name,
                    phone,
                    email,
                    address,
                    payment_method,
                    total,
                    status

                )
                VALUES(?,?,?,?,?,?,?)
                """,
                (
                    customer_name,
                    phone,
                    email,
                    address,
                    payment_method,
                    total,
                    "Preparing"
                )
            )

            order_id = cursor.lastrowid

            for item in order_items:

                cursor.execute(
                    """
                    INSERT INTO order_items(

                        order_id,
                        item_id,
                        item_name,
                        quantity,
                        price,
                        subtotal

                    )
                    VALUES(?,?,?,?,?,?)
                    """,
                    (
                        order_id,
                        item["item_id"],
                        item["item_name"],
                        item["quantity"],
                        item["price"],
                        item["subtotal"]
                    )
                )

        return order_id

    # =====================================================
    # Get All Orders
    # =====================================================

    def get_orders(self):

        with db.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM orders
                ORDER BY created_at DESC
                """
            )

            orders = []

            for row in cursor.fetchall():

                order = dict(row)

                cursor.execute(
                    """
                    SELECT

                        item_id,
                        item_name,
                        quantity,
                        price,
                        subtotal

                    FROM order_items

                    WHERE order_id=?
                    """,
                    (row["id"],)
                )

                order["items"] = [

                    dict(item)

                    for item in cursor.fetchall()

                ]

                orders.append(order)

        return orders

    # =====================================================
    # Get Single Order
    # =====================================================

    def get_order(self, order_id):

        with db.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM orders
                WHERE id=?
                """,
                (order_id,)
            )

            row = cursor.fetchone()

            if row is None:
                return None

            order = dict(row)

            cursor.execute(
                """
                SELECT

                    item_id,
                    item_name,
                    quantity,
                    price,
                    subtotal

                FROM order_items

                WHERE order_id=?
                """,
                (order_id,)
            )

            order["items"] = [

                dict(item)

                for item in cursor.fetchall()

            ]

            return order

    # =====================================================
    # Update Status
    # =====================================================

    def update_status(self, order_id, status):

        db.execute(
            """
            UPDATE orders

            SET status=?

            WHERE id=?
            """,
            (status, order_id)
        )

    # =====================================================
    # Delete Order
    # =====================================================

    def delete_order(self, order_id):

        with db.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM order_items WHERE order_id=?",
                (order_id,)
            )

            cursor.execute(
                "DELETE FROM orders WHERE id=?",
                (order_id,)
            )

    # =====================================================
    # Statistics
    # =====================================================

    def get_statistics(self):

        with db.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT

                    COUNT(*) AS total_orders,

                    IFNULL(SUM(total),0) AS revenue,

                    IFNULL(AVG(total),0) AS average_order

                FROM orders
                """
            )

            return dict(cursor.fetchone())
