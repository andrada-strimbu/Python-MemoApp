import sqlite3
from datetime import datetime

class Database:
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

def main():
        # Create an instance of DatabaseManager
        db_manager = Database()

        # Test create (save_memo)
        db_manager.save_memo("andrada", "Discuss project timelines.")
        db_manager.save_memo("carina", "Milk, eggs, bread")

        # Test read (load_latest_memo)
        latest_memo = db_manager.load_latest_memo()
        if latest_memo:
            print("Latest Memo:")
            print("ID:", latest_memo[0])
            print("Title:", latest_memo[1])
            print("Date:", latest_memo[2])
            print("Note:", latest_memo[3])
            print()

        # Test update (update_memo)
        update_id = 1  # Assuming memo with ID 1 exists
        db_manager.update_memo(update_id, "Updated Meeting Notes", "Discuss revised project timelines.")

        # Test read again to see the updated memo
        updated_memo = db_manager.load_memo_by_title("Shopping List")
        if updated_memo:
            print("Updated Memo:")
            print("ID:", updated_memo[0])
            print("Title:", updated_memo[1])
            print("Date:", updated_memo[2])
            print("Note:", updated_memo[3])
            print()

        # Test delete (delete_memo_by_title)


        # Test read again after deletion


        # Close the database connection
        db_manager.close_connection()

main()