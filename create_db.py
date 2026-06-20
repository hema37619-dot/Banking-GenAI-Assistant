import sqlite3
import os
from auth.hash_password import hash_password
from config import USERS_DB

os.makedirs(os.path.dirname(USERS_DB), exist_ok=True)

conn = sqlite3.connect(USERS_DB)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

users = [
    ("admin",    "admin123",   "admin"),
    ("manager1", "manager123", "manager"),
    ("clerk1",   "clerk123",   "clerk"),
]

for username, password, role in users:
    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES (?, ?, ?)
    """, (username, hash_password(password), role))

conn.commit()
conn.close()
print("✅ users.db created successfully")