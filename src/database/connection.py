import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    db_path = "data/feedix.db"
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()
