import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            input_value REAL,
            prediction_result REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_prediction(val, pred):
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (timestamp, input_value, prediction_result)
        VALUES (?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), val, pred))
    conn.commit()
    conn.close()

def predict(n):
    res = n * 2
    log_prediction(n, res)
    return res

if __name__ == "__main__":
    init_db()
    predict(42)
