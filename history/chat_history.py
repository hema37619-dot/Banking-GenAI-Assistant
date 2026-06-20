import sqlite3

DB_PATH = "database/chat_history.db"

def init_chat_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            question TEXT,
            answer TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_history(username, question, answer):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO chat_history (username, question, answer)
        VALUES (?, ?, ?)
    """, (username, question, answer))
    conn.commit()
    conn.close()

def get_all_history():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT username, question, answer, timestamp FROM chat_history ORDER BY timestamp DESC")
    rows = cur.fetchall()
    conn.close()
    return [{"username": r[0], "question": r[1], "answer": r[2], "timestamp": r[3]} for r in rows]

def get_user_history(username):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT question, answer, timestamp FROM chat_history WHERE username=? ORDER BY timestamp DESC", (username,))
    rows = cur.fetchall()
    conn.close()
    return [{"question": r[0], "answer": r[1], "timestamp": r[2]} for r in rows]