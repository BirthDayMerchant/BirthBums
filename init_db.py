import sqlite3

# Connect to SQLite (this creates the file if it doesn't exist)
conn = sqlite3.connect('birthdays.db')
cursor = conn.cursor()

# Create the students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dob DATE NOT NULL
    )
''')

# Create the users table for logins
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        name TEXT NOT NULL,
        room_no TEXT,
        dob DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS birthday_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        room_no TEXT,
        proof TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        suggestion_text TEXT NOT NULL
    )
''')

# Insert some dummy data (Format: YYYY-MM-DD)
dummy_data = [
    ('Alice', '2005-09-15'), # Set this close to today's date to test "upcoming"
    ('Bob', '2006-10-22'),
    ('Charlie', '2005-01-05')
]

cursor.executemany('INSERT INTO students (name, dob) VALUES (?, ?)', dummy_data)
conn.commit()
conn.close()

print("Database initialized successfully!")