import sqlite3
conn= sqlite3.connect("database/users.db")
cur=conn.cursor()
cur.execute("DELETE FROM users")
conn.commit()
print("All users have been deleted from the database.")
conn.close()