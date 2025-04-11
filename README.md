# Ride Sharing Analytics

This is a data-driven web application built using Flask that provides insights into ride-sharing activity. It processes ride data and presents analytics like pricing trends, distance distribution, and more.

## Features
- Ride data ingestion and storage
- Data analysis and basic visualization
- SQLite database integration
- Flask-powered web interface

## Technologies Used
- Python, Flask
- SQLite3
- pandas
- HTML/CSS (Jinja templating)

## How to Run Locally

```bash
git clone https://github.com/ritikrauniyar93/ride-sharing-analytics.git
cd ride-sharing-analytics
pip install -r requirements.txt
python database_setup.py
python insert_sample_data.py
python app.py
