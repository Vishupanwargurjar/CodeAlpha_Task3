# CodeAlpha Task 3:

This repository contains my submission for Task 3 of the **CodeAlpha Cybersecurity Internship**.

## 👨‍💻 Created By:
**Vishu Panwar**

## 📌 Task Objective:
Analyze and fix security vulnerabilities in a login system implemented with Python and SQLite.

### ✅ Insecure Version:
- Demonstrates SQL Injection vulnerability.
- Input like `' OR '1'='1` bypasses authentication.

### 🔐 Secure Version:
- Uses parameterized queries (`?`) to prevent SQL injection.
- Validates credentials properly using safe query methods.

## 📝 Files Included:
- `create_db.py` → Initializes the database and inserts test user.
- `insecure_code_sample.py` → Vulnerable login system (for demonstration only).
- `secure_code_review.py` → Secure, injection-proof version of login system.
- `users.db` → SQLite database file (auto-generated).

## 💡 What I Learned:
- How SQL Injection works in real-world systems.
- Importance of secure coding practices.
- How to fix vulnerabilities using parameterized queries.

## 📂 How to Run:

```bash
python3 create_db.py           # Step 1: Create the database
python3 insecure_code_sample.py   # Step 2: Run insecure version (check vulnerability)
python3 secure_code_review.py     # Step 3: Run secure version (enter correct/incorrect inputs)
