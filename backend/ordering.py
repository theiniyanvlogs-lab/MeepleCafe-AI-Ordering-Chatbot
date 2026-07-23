"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Order Manager
Version : 2.0
=========================================================
"""

import sqlite3
import os
import pandas as pd


class OrderManager:

    def __init__(self):

        base_dir = os.path.dirname(__file__)

        self.db_path = os.path.join(
            base_dir,
            "..",
            "data",
            "orders.db"
        )

        self.menu_path = os.path.join(
            base_dir,
            "..",
            "data",
            "menu.csv"
        )

        self._initialize_database()

    # -----------------------------------------------------
    # Database Initialization
    # -----------------------------------------------------

    def _initialize_database(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            phone TEXT,
            email TEXT,
            address TEXT,
            payment_method TEXT,
            total REAL,
            status TEXT DEFAULT 'Preparing',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            item_id INTEGER,
            item_name TEXT,
            quantity INTEGER,
            price REAL,
            subtotal REAL
        )
        """)

        conn.commit()
        conn.close()

    # -----------------------------------------------------
    # Place Order
    # -----------------------------------------------------

    def place_order(
        self,
        customer_name,
        phone,
        email,
        address,
        payment_method,
        items
    ):

        menu = pd.read_csv(self.menu_path)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        total = 0
        order_items = []

        for item in items:

            menu_item = menu[
                menu["Item_ID"] == item["id"]
            ]

            if menu_item.empty:
                continue

            row = menu_item.iloc[0]

            price = float(row["Price"])

            subtotal = price * item["quantity"]

            total += subtotal

            order_items.append({
                "item_id": int(row["Item_ID"]),
                "item_name": row["Item_Name"],
                "price": price,
                "quantity": item["quantity"],
                "subtotal": subtotal
            })

        cursor.execute("""
        INSERT INTO orders(
            customer_name,
            phone,
            email,
            address,
            payment_method,
            total
        )
        VALUES(?,?,?,?,?,?)
        """, (
            customer_name,
            phone,
            email,
            address,
            payment_method,
            total
        ))

        order_id = cursor.lastrowid

        for item in order_items:

            cursor.execute("""
            INSERT INTO order_items(
                order_id,
                item_id,
                item_name,
                quantity,
                price,
                subtotal
            )
            VALUES(?,?,?,?,?,?)
            """, (
                order_id,
                item["item_id"],
                item["item_name"],
                item["quantity"],
                item["price"],
                item["subtotal"]
            ))

        conn.commit()
        conn.close()

        return order_id

    # -----------------------------------------------------
    # Get Orders
    # -----------------------------------------------------

    def get_orders(self):

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM orders
        ORDER BY created_at DESC
        """)

        orders = []

        for row in cursor.fetchall():

            order = dict(row)

            cursor.execute("""
            SELECT
                item_id,
                item_name,
                quantity,
                price,
                subtotal
            FROM order_items
            WHERE order_id=?
            """, (row["id"],))

            order["items"] = [
                dict(item)
                for item in cursor.fetchall()
            ]

            orders.append(order)

        conn.close()

        return orders
