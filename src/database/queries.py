import sqlite3
from database.connection import get_db_connection 

##############
## CHANNELS ##
##############

def create_channel(values):
    with get_db_connection() as conn:
        sql = """
            INSERT INTO channels(
                id, 
                title, 
                link
            )
            VALUES(?,?,?)
        """
        conn.execute(sql, values)
        conn.commit()

def get_channel_id_by_link(value):
    with get_db_connection() as conn:
        sql = """
            SELECT id FROM channels WHERE link=?
        """
        cur = conn.cursor()
        cur.execute(sql, value)
        result = cur.fetchone()
        if result:
            return result[0]

##############
## ARTICLES ##
##############

def create_article(values):
    with get_db_connection() as conn:
        sql = """
            INSERT INTO articles(
                id, 
                channel_id, 
                status, 
                title, 
                date, 
                link, 
                description
            )
            VALUES(?,?,?,?,?,?,?)
        """
        conn.execute(sql, values)
        conn.commit()

def get_article_by_title(value):
    with get_db_connection() as conn:
        sql = """
            SELECT * FROM articles WHERE title=?
        """
        cur = conn.cursor()
        cur.execute(sql, value)
        result = cur.fetchone()
        if result: 
            return result[0]

def get_articles_by_status(value):
    with get_db_connection() as conn:
        sql = """
            SELECT * FROM articles WHERE status=? 
        """
        cur = conn.cursor()
        cur.execute(sql, value)
        result = cur.fetchall()
        if result:
            return result

def update_article_score_by_id(values):
    with get_db_connection() as conn:
        sql = """
            UPDATE articles
            SET status=?, score=?
            WHERE id=?
        """
        conn.execute(sql, values)
        conn.commit()

def update_article_summary_by_id(values):
    with get_db_connection() as conn:
        sql = """
            UPDATE articles
            SET status=?, summary=?
            WHERE id=?
        """
        conn.execute(sql, values)
        conn.commit()

def delete_article_by_id(value):
    with get_db_connection() as conn:
        sql = """
            DELETE FROM articles
            WHERE id=?
        """
        conn.execute(sql, value)
        conn.commit()
