import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Taking input
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# ✅ Proper tuple formatting
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

result = cursor.fetchone()

if result:
    print("✅ Login successful!")
else:
    print("❌ Invalid credentials!")

conn.close()
