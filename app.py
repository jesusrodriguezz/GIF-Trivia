#Created by Maria Barrera

from flask import Flask
from flask import render_template
from flask import request
import sqlite3

from gif import getGif
from migration import create_table, drop_all_tables

app = Flask(__name__)

drop_all_tables()
create_table()

# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/score", methods = ['POST'])
def score():
    if request.method == 'POST':
        try:
            username = request.form['username']
            score = request.form['score']
            attempts = request.form['attempts']
            status = request.form['status']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO score (username, score, attempts, status) VALUES (?,?,?,?)",
                            (username, score, attempts, status))
                con.commit()

            return "Score added successfully"
        except Exception as e:
            print("An error occurred:", str(e))
            return "Error adding score"

@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT rowid, * FROM score")

    rows = cur.fetchall()
    con.close()
    return render_template("list.html",rows=rows)

@app.route('/gif', methods = ['GET'])
def gif():
    url, title = getGif()
    return {"url": url, "title": title}
