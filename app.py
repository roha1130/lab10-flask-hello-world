
import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from roha1130 in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_bball_db_user:dSQtWQ3PQ28wsIVf6vp3BoiF15FB474i@dpg-co4ebakf7o1s738rff3g-a/lab10_bball_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://lab10_bball_db_user:dSQtWQ3PQ28wsIVf6vp3BoiF15FB474i@dpg-co4ebakf7o1s738rff3g-a/lab10_bball_db")
    curr = conn.cursor()
    curr.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://lab10_bball_db_user:dSQtWQ3PQ28wsIVf6vp3BoiF15FB474i@dpg-co4ebakf7o1s738rff3g-a/lab10_bball_db")
    curr = conn.cursor()
    curr.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"