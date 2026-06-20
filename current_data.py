import sqlite3
conn= sqlite3.connect("database/users.db")
cur=conn.cursor()
cur.execute("SELECT * FROM users")
users=cur.fetchall()
print("Current users in the database:")
print(users)