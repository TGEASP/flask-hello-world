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


@app.route('/db_create')
def db_create():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Basketball (
                First varchar(255),
                Last varchar(255),
                City varchar(255),
                Name varchar(255),
                Number int
            );
        """)

        conn.commit()
        return "Basketball Table Successfully Created"

    except Exception as e:
        if conn:
            conn.rollback()
        return f"Database error: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


@app.route('/db_insert')
def db_insert():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Basketball (First, Last, City, Name, Number)
            VALUES
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        """)

        conn.commit()
        return "Basketball Table Successfully Populated"

    except Exception as e:
        if conn:
            conn.rollback()
        return f"Database error: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


@app.route('/db_select')
def db_select():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        cur.execute("SELECT * FROM Basketball;")
        records = cur.fetchall()

        response_string = "<table border='1'>"

        for player in records:
            response_string += "<tr>"
            for info in player:
                response_string += f"<td>{info}</td>"
            response_string += "</tr>"

        response_string += "</table>"
        return response_string

    except Exception as e:
        return f"Database error: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


@app.route('/db_drop')
def db_drop():
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        cur.execute("DROP TABLE Basketball;")

        conn.commit()
        return "Basketball Table Successfully Dropped"

    except Exception as e:
        if conn:
            conn.rollback()
        return f"Database error: {e}"

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(debug=True)
