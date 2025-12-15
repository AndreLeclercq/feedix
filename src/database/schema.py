import sqlite3
from database.connection import get_db_connection  

def create_tables():
    schemas = [
        """
        CREATE TABLE IF NOT EXISTS channels (
            id TEXT PRIMARY KEY,
            title VARCHAR(250) NOT NULL,
            link VARCHAR(250) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS articles (
            id TEXT PRIMARY KEY,
            channel_id TEXT NOT NULL,
            status VARCHAR(30) NOT NULL,
            title VARCHAR(250) NOT NULL,
            date DATETIME NOT NULL,
            link VARCHAR(250) NOT NULL,
            description TEXT NOT NULL,
            score REAL,
            summary TEXT,
            FOREIGN KEY (channel_id) REFERENCES channels(id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
        );
        """,
        """
        CREATE INDEX IF NOT EXISTS idx_articles_status ON articles(status);
        """,
        """
        CREATE INDEX IF NOT EXISTS idx_channels_link on channels(link);
        """
    ]

    with get_db_connection() as conn:
        for schema in schemas:
            conn.execute(schema)

