
import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from roha1130 in 3308'

@app.route('db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_bball_db_user:dSQtWQ3PQ28wsIVf6vp3BoiF15FB474i@dpg-co4ebakf7o1s738rff3g-a/lab10_bball_db")
    conn.close()
    return "Database Connection Successful"