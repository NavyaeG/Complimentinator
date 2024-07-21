import sqlite3
import os

class Table:
    db_path=None 

    @staticmethod
    def init_db_path(db_path):
        if not os.path.exists(db_path):
            os.makedirs(db_path)
        Table.db_path = os.path.join(db_path, 'compliments.db')

    @staticmethod
    def create_table():
        conn = sqlite3.connect(Table.db_path)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS compliments (
            sl INTEGER PRIMARY KEY,
            compliment TEXT,
            used TEXT
        )""")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM compliments")
        count = cursor.fetchone()[0]
        if count == 0:
            compliments = [
                (1, "You look nice", "False")       
            ]
            cursor.executemany("INSERT INTO compliments (sl, compliment, used) VALUES (?, ?, ?)", compliments)
        
        conn.commit()
        conn.close()

    @staticmethod
    def fetch_compliment():
        conn = sqlite3.connect(Table.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT sl, compliment FROM compliments WHERE used = 'False' ORDER BY RANDOM() LIMIT 1")
        compliment = cursor.fetchone()
        
        if compliment is not None:
            cursor.execute("UPDATE compliments SET used = 'True' WHERE sl = ?", (compliment[0],))
            conn.commit()
            conn.close()
            return compliment[1]
        else:
            cursor.execute("UPDATE compliments SET used = 'False'")
            conn.commit()
            conn.close()
            return Table.fetch_compliment()