import flask
from flask import Flask, redirect, render_template, request
import sqlite3

app = Flask(__name__)

def connect_db():
  sql = sqlite3.connect('/database.db')

SPORTS = [
  "Basketball",
  "Soccer",
  "Ultimate Frisbee"
]

@app.route("/")
def index():
  return render_template("index.html", sports = SPORTS)


 

