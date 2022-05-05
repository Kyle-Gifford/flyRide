from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
from credenitals import *

ONID = credenitals.onid #onid (i.e. doejo)
MYSQL_PASSWORD = credenitals.password #last 4 digits of onid
PORT = credenitals.port #enter port number

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340' + ONID
app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD 
app.config['MYSQL_DB'] = 'cs340' + ONID
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def root():
    query = "SELECT * FROM diagnostic;"
    query1 = 'DROP TABLE IF EXISTS diagnostic;';
    query2 = 'CREATE TABLE diagnostic(id INT PRIMARY KEY AUTO_INCREMENT, text VARCHAR(255) NOT NULL);';
    query3 = 'INSERT INTO diagnostic (text) VALUES ("MySQL is working!")';
    query4 = 'SELECT * FROM diagnostic;';
    cur = mysql.connection.cursor()
    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    results = cur.fetchall()

    return results[0]


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=PORT, debug=True)