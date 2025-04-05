# app.py

from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def fetch_data():
    conn = sqlite3.connect('rides.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM rides')
    total_rides = cursor.fetchone()[0]

    cursor.execute('SELECT SUM(price) FROM rides')
    total_earnings = cursor.fetchone()[0]

    cursor.execute('SELECT source, COUNT(*) FROM rides GROUP BY source ORDER BY COUNT(*) DESC LIMIT 1')
    top_source = cursor.fetchone()[0]

    cursor.execute('SELECT driver_id, SUM(price) FROM rides GROUP BY driver_id')
    rows = cursor.fetchall()
    driver_earnings = {row[0]: row[1] for row in rows}

    conn.close()

    return {
        'total_rides': total_rides,
        'total_earnings': total_earnings,
        'top_source': top_source,
        'driver_earnings': driver_earnings
    }

@app.route('/')
def dashboard():
    data = fetch_data()
    return render_template('dashboard.html', **data)

@app.route('/api/data')
def api_data():
    data = fetch_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
