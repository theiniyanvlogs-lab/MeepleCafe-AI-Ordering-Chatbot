"""
=========================================================
Meeple Cafe AI Ordering Chatbot
Database Manager
Version : 2.0
=========================================================
"""

import os
import sqlite3
from contextlib import contextmanager


class DatabaseManager:
    """
    SQLite Database Manager

    Features
    --------
    ✔ Automatic database creation
    ✔ Table initialization
    ✔ Context manager support
    ✔ Execute queries
    ✔ Fetch one
    ✔ Fetch all
    ✔ Transaction handling
    """

    def __init__(self):

        self.db_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "data",
            "orders.db",
        )

        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

        self.initialize_database()

    # =====================================================
    # Connection
    # =====================================================

    def connect(self):

        conn = sqlite3.connect(self.db_path)

        conn.row_factory = sqlite3.Row

        return conn

    # =====================================================
    # Context Manager
    # =====================================================

    @contextmanager
    def get_connection(self):

        conn = self.connect()

        try:

            yield conn

            conn.commit()

        except Exception:

            conn.rollback()

            raise

        finally:

            conn.close()

    # =====================================================
    # Initialize Database
    # =====================================================

    def initialize_database(self):

        with self.get_connection() as conn:

            cursor = conn.cursor()

            # -------------------------------
            # Orders
            # -------------------------------

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS orders(

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    customer_name TEXT NOT NULL,

                    phone TEXT NOT NULL,

                    email TEXT,

                    address TEXT NOT NULL,

                    payment_method TEXT NOT NULL,

                    total REAL NOT NULL,

                    status TEXT DEFAULT 'Preparing',

                    created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

            # -------------------------------
            # Order Items
            # -------------------------------

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS order_items(

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    order_id INTEGER NOT NULL,

                    item_id INTEGER NOT NULL,

                    item_name TEXT NOT NULL,

                    quantity INTEGER NOT NULL,

                    price REAL NOT NULL,

                    subtotal REAL NOT NULL,

                    FOREIGN KEY(order_id)
                    REFERENCES orders(id)
                    ON DELETE CASCADE
                )
                """
            )

    # =====================================================
    # Execute
    # =====================================================

    def execute(self, query, params=()):

        with self.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(query, params)

            return cursor.lastrowid

    # =====================================================
    # Fetch One
    # =====================================================

    def fetch_one(self, query, params=()):

        with self.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(query, params)

            row = cursor.fetchone()

            return dict(row) if row else None

    # =====================================================
    # Fetch All
    # =====================================================

    def fetch_all(self, query, params=()):

        with self.get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute(query, params)

            rows = cursor.fetchall()

            return [dict(row) for row in rows]


# =========================================================
# Singleton Instance
# =========================================================

db = DatabaseManager()
