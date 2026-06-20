import sqlite3

from auth.hash_password import hash_password
DB = "database/users.db"
def register_user(username,password,role):

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute("""
           INSERT INTO users
            (
                username,
                password,
                role
            )
            VALUES (?, ?, ?)
    """, 
    (
        username,
        hashed, 
        role
    ))

    conn.commit()
    conn.close()
    return