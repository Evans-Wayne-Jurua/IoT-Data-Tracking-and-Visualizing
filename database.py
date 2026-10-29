import sqlite3

conn = sqlite3.connect(data/readings.db)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS readings(
    id INTEGER PRIMARY KEY,
    voltage REAL,
    current REAL,
    power REAL)""")

conn.commit()
conn.close()