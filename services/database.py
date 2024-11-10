import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self._create_feedback_table()

    def _create_feedback_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY,
            type TEXT,
            message TEXT
        )''')
        self.conn.commit()

    def add_feedback(self, feedback_type, message):
        self.cursor.execute("INSERT INTO feedback (type, message) VALUES (?, ?)", (feedback_type, message))
        self.conn.commit()

    def close(self):
        self.conn.close()

db = Database()

