import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/linkedin.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    topic TEXT,
    post TEXT,
    image TEXT
)
""")

conn.commit()


def save_post(date, topic, post, image):

    cursor.execute(
        """
        INSERT INTO posts(date,topic,post,image)
        VALUES(?,?,?,?)
        """,
        (date, topic, post, image)
    )

    conn.commit()


def get_last_posts(limit=10):

    cursor.execute(
        """
        SELECT post
        FROM posts
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    return [row[0] for row in cursor.fetchall()]