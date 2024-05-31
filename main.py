from flask import Flask, render_template
from flask_session import Session

API_BASEURL = "https://carterapi.pythonanywhere.com/"
API_KEY = "abc"

app = Flask(__name__)

Session(app)


@app.route("/")
def index():
    return render_template("main/index.html", title="Home")


if __name__ == "__main__":
    app.run()
