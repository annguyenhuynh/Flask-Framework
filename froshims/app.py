import flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
  name = request.form.get("name")
  sport = request.form.get("sports")
  print(f"Name: {name}, Sport: {sport}")  # Print to terminal for debugging
    
  if not name or sport=="":
    return render_template("failure.html")
  return render_template('success.html')
  
if __name__ == '__main__':
  app.run(debug=True)
