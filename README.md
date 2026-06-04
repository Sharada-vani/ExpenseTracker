# API Integration & Workflow Automation

Author:Sharada Vani S  
Tech Stack: Python, REST APIs, JSON, SQLite

# Project Overview
A Python automation script that fetches live weather data 
from the OpenWeatherMap REST API, parses the JSON response, 
and auto-saves structured records to a local SQLite database.

## Data Flow
OpenWeatherMap API
↓
GET request (Python requests library)
↓
JSON Response parsed
↓
Structured records extracted
↓
SQLite Database (weather_data.db)
↓
Console report displayed
---

## Features
- Fetches real-time weather for multiple cities in one run
- Parses JSON — extracts temperature, humidity, wind speed
- Auto-saves all records to SQLite with timestamp
- Error handling for invalid API key, city not found,
  timeout, and no internet
- Displays a formatted report of all saved records

---

## Error Handling
| Error | Status Code | Handled |
|---|---|---|
| Invalid API key | 401 
| City not found | 404 
| Too many requests | 429
| No internet | ConnectionError|
| Request timeout | Timeout 

---

# Setup & Run

# 1. Install dependency
pip install requests

# 2. Get free API key
- Go to openweathermap.org
- Sign up free → API Keys tab
- Copy your key

# 3. Add your API key
Open weather_integration.py and replace:
API_KEY = "YOUR_API_KEY_HERE"

# 4. Run the script
python weather_integration.py

---

# Sample Output
🚀 Starting Weather API Integration

 Database ready: weather_data.db

Processing: Bellary
Fetched data for Bellary — Status: 200 OK
Saved: Bellary — 32.5°C, clear sky

Completed — 5 saved, 0 failed

=================================================================
ID   City           Temp  Humidity   Wind  Description
=================================================================
1    Bellary        32.5°C      45%   4.2m/s  clear sky
2    Bangalore      24.1°C      70%   3.1m/s  few clouds
=================================================================
Total records: 2

---

## Database Schema
CREATE TABLE weather_records (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    city        TEXT NOT NULL,
    temperature REAL,
    humidity    INTEGER,
    wind_speed  REAL,
    description TEXT,
    fetched_at  TEXT
);
