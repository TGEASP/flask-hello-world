from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

@app.route('/')
def hello_world():
    return 'Hello, World from Abhinavsai Parsi in 3308'

@app.route('/db_test')
def db_test():
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database Connection Successful"
    except Exception as e:
        return f"Database Connection Failed: {e}"
    finally:
        if conn:
            conn.close()
