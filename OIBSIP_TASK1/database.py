import sqlite3

DB_FILE = "bmi_data.sqlite"


def init_db():
    """Create BMI table if not exists."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bmi_records(
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            height REAL,
            weight REAL,
            bmi REAL,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()


def insert_record(height, weight, bmi, category):
    """Insert a new BMI record into the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bmi_records(height, weight, bmi, category)
        VALUES(?,?,?,?) 
    ''',(height, weight, bmi, category))
    conn.commit()
    conn.close()


def fetch_history():
    """Fetch BMI history from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT timestamp, height, weight, bmi, category FROM bmi_records
        ORDER BY timestamp ASC
    ''')
    history = cursor.fetchall()
    conn.close()
    return history
