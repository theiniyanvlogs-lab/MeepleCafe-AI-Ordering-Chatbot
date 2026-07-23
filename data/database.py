"""
=========================================================
Meeple Cafe AI Ordering Chatbot
SQLite Database Manager
Version : 1.0
=========================================================
"""

import sqlite3
import os


class DatabaseManager:
    """
    Handles all SQLite database operations.
    """

    def __init__(self):

        db_folder = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data"
        )

        os.makedirs(db_folder, exist_ok=True)

        self.db_path = os.path.join(
            db_folder,
            "restaurant.db"
        )

        self.create_tables()

    # --------------------------------------------------

    def connect(self):

        return sqlite3.connect(self.db_path)

    # --------------------------------------------------

    def create_tables(self):

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (

            order_id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id TEXT,

            customer_name TEXT,

            phone TEXT,

            dining_type TEXT,

            table_number TEXT,

            address TEXT,

            total REAL,

            status TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            order_id INTEGER,

            item_name TEXT,

            quantity INTEGER,

            price REAL,

            FOREIGN KEY(order_id)
            REFERENCES orders(order_id)

        )
        """)

        conn.commit()
        conn.close()

    # --------------------------------------------------

    def create_order(
        self,
        session_id,
        customer_name,
        phone,
        dining_type,
        table_number,
        address,
        total,
        status="Pending"
    ):

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO orders (

            session_id,
            customer_name,
            phone,
            dining_type,
            table_number,
            address,
            total,
            status

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)

        """, (

            session_id,
            customer_name,
            phone,
            dining_type,
            table_number,
            address,
            total,
            status

        ))

        order_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return order_id

    # --------------------------------------------------

    def add_order_item(

        self,
        order_id,
        item_name,
        quantity,
        price

    ):

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO order_items (

            order_id,
            item_name,
            quantity,
            price

        )

        VALUES (?, ?, ?, ?)

        """, (

            order_id,
            item_name,
            quantity,
            price

        ))

        conn.commit()
        conn.close()

    # --------------------------------------------------

    def get_order(self, order_id):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""

        SELECT *

        FROM orders

        WHERE order_id=?

        """, (order_id,))

        order = cursor.fetchone()

        conn.close()

        return order

    # --------------------------------------------------

    def get_order_items(self, order_id):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        item_name,
        quantity,
        price

        FROM order_items

        WHERE order_id=?

        """, (order_id,))

        items = cursor.fetchall()

        conn.close()

        return items

    # --------------------------------------------------

    def update_status(

        self,
        order_id,
        status

    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute("""

        UPDATE orders

        SET status=?

        WHERE order_id=?

        """, (

            status,
            order_id

        ))

        conn.commit()

        conn.close()
