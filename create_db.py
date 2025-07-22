import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

# Add a test user
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")

conn.commit()
conn.close()

print("Database created successfully.")
