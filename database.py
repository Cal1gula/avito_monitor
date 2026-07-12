import sqlite3
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DB_FILE = DATA_DIR / "avito.db"


class Database:

    def __init__(self):

        self.conn = sqlite3.connect(DB_FILE)

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS items(
                id TEXT PRIMARY KEY,
                title TEXT,
                price INTEGER,
                city TEXT,
                url TEXT,
                search_url TEXT,
                found_at TEXT
            )
        """)

        self.conn.commit()

    def add(self, item):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO items
            (
                id,
                title,
                price,
                city,
                url,
                search_url,
                found_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item["id"],
                item["title"],
                item["price"],
                item["city"],
                item["url"],
                item["search_url"],
                item["found_at"]
            )
        )

        self.conn.commit()

    def exists(self, item_id):

        self.cursor.execute(
            "SELECT 1 FROM items WHERE id=?",
            (item_id,)
        )

        return self.cursor.fetchone() is not None

    def get(self, item_id):

        self.cursor.execute(
            """
            SELECT
                id,
                title,
                price,
                city,
                url,
                search_url,
                found_at
            FROM items
            WHERE id=?
            """,
            (item_id,)
        )

        row = self.cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "title": row[1],
            "price": row[2],
            "city": row[3],
            "url": row[4],
            "search_url": row[5],
            "found_at": row[6]
        }            