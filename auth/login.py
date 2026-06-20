import sqlite3
from auth.hash_password import verify_password, hash_password
from config import USERS_DB

def authenticate(username, password):
    conn = sqlite3.connect(USERS_DB)
    cur = conn.cursor()
    cur.execute("""
        SELECT password, role FROM users WHERE username=?
    """, (username,))
    user = cur.fetchone()
    conn.close()

    if user:
        db_password = user[0]
        role = user[1]
        if verify_password(password, db_password):
            return role
    return None

def add_clerk(username, password):
    try:
        conn = sqlite3.connect(USERS_DB)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, hash_password(password), "clerk"))
        conn.commit()
        conn.close()
        return True, "✅ Clerk added successfully."
    except sqlite3.IntegrityError:
        return False, "❌ Username already exists. Choose a different username."