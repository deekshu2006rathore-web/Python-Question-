import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Create table if not exists (ensures no error)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# --- INSERT ---
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 22))
print("Inserted Alice and Bob.")

# --- UPDATE ---
cursor.execute("UPDATE students SET age = 21 WHERE name = 'Alice'")
print("Updated Alice's age to 21.")

# --- DELETE ---
cursor.execute("DELETE FROM students WHERE name = 'Bob'")
print("Deleted Bob.")

# --- SELECT ---
cursor.execute("SELECT * FROM students")
print("\nRecords after operations:")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()