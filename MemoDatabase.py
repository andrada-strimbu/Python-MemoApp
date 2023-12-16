import sqlite3
from datetime import datetime

class MemoDatabase:
    def __init__(self, db_file='memo.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS MemoDatabase 
                               (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                note TEXT,
                                date DATE
                               )
                            ''')

    def save_memo(self, title, note):
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("INSERT INTO MemoDatabase (title, note, date) VALUES (?, ?, ?)", (title, note, current_date))
        self.conn.commit()

    def delete_memo_by_title(self, title):
        self.cursor.execute("DELETE FROM MemoDatabase WHERE title=?", (title,))
        self.conn.commit()

    def update_memo(self, memo_id, title, note):
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("UPDATE MemoDatabase SET title=?, note=?, date=? WHERE id=?",
                            (title, note, current_date, memo_id))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

    def load_latest_memo(self):
        self.cursor.execute("SELECT * FROM MemoDatabase ORDER BY id DESC LIMIT 1")
        result = self.cursor.fetchone()
        return result if result else None

    def load_memo_by_title(self, title):
        self.cursor.execute("SELECT * FROM MemoDatabase WHERE title=?", (title,))
        result = self.cursor.fetchone()
        return result if result else None
    def get_all_titles(self):
        self.cursor.execute("SELECT title FROM MemoDatabase")
        result= self.cursor.fetchall()
        return result if result else None

