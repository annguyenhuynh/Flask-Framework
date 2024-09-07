from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/greet",methods=["POST"])
def greet():
  name = request.args.get("name")
  return render_template("greet.html", placeholder=name)



if __name__ == '__main__':
  app.run(debug=True)
