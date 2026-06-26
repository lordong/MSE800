from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/hello_template/<name>")
def hello_template(name):
    return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
