# insert_sample_data.py

import sqlite3
import random
from datetime import datetime
import time

# Sample values for simulation
drivers = ['D101', 'D102', 'D103', 'D104']
sources = ['Patna Junction', 'Bailey Road', 'Boring Road', 'Kankarbagh']
destinations = ['Airport', 'Gandhi Maidan', 'Danapur', 'Fraser Road']

def insert_ride():
    conn = sqlite3.connect('rides.db')
    cursor = conn.cursor()

    driver_id = random.choice(drivers)
    source = random.choice(sources)
    destination = random.choice(destinations)
    price = round(random.uniform(100, 500), 2)
    timestamp = datetime.now()

    cursor.execute('''
    INSERT INTO rides (driver_id, source, destination, price, timestamp)
    VALUES (?, ?, ?, ?, ?)
    ''', (driver_id, source, destination, price, timestamp))

    conn.commit()
    conn.close()
    print(f"✅ Ride added: {driver_id}, ₹{price}, {source} ➡ {destination}, 🕒 {timestamp}")

# Simulate adding a new ride every 3 seconds
for _ in range(5):  # Insert 5 sample rides (increase if needed)
    insert_ride()
    time.sleep(3)
