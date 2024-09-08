import flask
from flask import Flask, redirect, render_template, request, g
import sqlite3

app = Flask(__name__)

SPORTS = [
  "Basketball",
  "Soccer",
  "Ultimate Frisbee"
]

DATABASE='database.db'
def get_db():
    """ Create a new database connection for each request. """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn 


def init_db():
    """ Initialize the database schema. """
    conn = get_db()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS registrants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sport TEXT NOT NULL
            )
        ''')
init_db()


@app.route("/")
def index():
  return render_template("index.html", sports = SPORTS)

@app.route("/deregister", methods=["POST"])
def deregister():

  #Forget registrants
  id = request.form.get("id")
  if id:
    conn = get_db()
    with conn:
      conn.execute("DELETE FROM registrants WHERE id = ? ", (id))
  return redirect("/registrants")

@app.route("/register", methods=['POST'])
def register():
  
  #Validate submission
  name = request.form.get("name")
  sport = request.form.get("sport")
  if not name or sport not in SPORTS:
    return render_template("failure.html")
  
  conn=get_db()
  #Remember registrants
  with conn:
    conn.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))
  #Confirm registration
  return redirect("/registrants")

@app.route("/registrants")
def registrants():
  conn = get_db()
  cur = conn.execute("SELECT * FROM registrants")
  registrants = cur.fetchall()
  return render_template("registrants.html",registrants=registrants)

if __name__ == "__main__":
  app.run(debug=True)


 

