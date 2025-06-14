
import sqlite3

def init_memory():
    conn = sqlite3.connect("fba_memory.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY,
        question TEXT,
        response TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def save_interaction(question, response):
    conn = sqlite3.connect("fba_memory.db")
    c = conn.cursor()
    c.execute("INSERT INTO memory (question, response) VALUES (?, ?)", (question, str(response)))
    conn.commit()
    conn.close()


def get_last_interactions(limit=5):
    conn = sqlite3.connect("fba_memory.db")
    c = conn.cursor()
    c.execute("SELECT question, response FROM memory ORDER BY created_at DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows
