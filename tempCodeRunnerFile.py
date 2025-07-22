import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # VULNERABLE: SQL injection possible here
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed.")
    
    conn.close()

# Example use (dangerous inputs)
login("admin", "1234' OR '1'='1")
