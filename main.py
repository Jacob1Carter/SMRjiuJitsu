from flask import Flask, render_template
from flask_session import Session

API_BASEURL = "http://127.0.0.1:5000/"
API_KEY = "abc"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main/index.html", title="Home")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5022)
