# database_setup.py

import sqlite3

# Connect to SQLite database (it will create the DB file if it doesn't exist)
conn = sqlite3.connect('rides.db')

# Create a cursor object
cursor = conn.cursor()

# Create table for rides
cursor.execute('''
CREATE TABLE IF NOT EXISTS rides (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id TEXT NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    price REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database and table 'rides' created successfully.")
