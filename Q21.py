import sqlite3

try:
    # Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Create table with IF NOT EXISTS to avoid errors if table already present
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')
    print("Table 'students' created successfully (or already exists).")

    # Optional: Verify by fetching table info
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';")
    if cursor.fetchone():
        print("Verification: Table exists in database.")

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")