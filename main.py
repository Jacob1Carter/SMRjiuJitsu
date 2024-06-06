from flask import Flask, render_template, request
from flask_session import Session
import requests
import json

API_BASEURL = "http://127.0.0.1:5000/"
HEADERS = {
    'x-api-key': "99PHmE43N3D64vFU82458rAf3i6Ud243",
    'Content-Type': 'application/json'
}
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main/index.html", title="Home")


@app.route("/login")
def login():
    return render_template("main/login-register.html", title=" SMRJJ Login", page="login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        request_data = {
            "username": username,
            "email": email,
        }

        try:
            response = requests.post(f"{API_BASEURL}/get/jiujitsu-user-exists", headers=HEADERS, json=request_data)
            try:
                response.json()
            except requests.exceptions.JSONDecodeError as e:
                return "API response error. Please try again later.<br><br>" + str(response) + "<br><br>" + str(e)
            if response.json()["result"] == "failed":
                if response.json()["error"] == "Unauthorized":
                    return "Unauthorized. Please try again later.<br><br>" + str(response.json())
                else:
                    return "API error. Please try again later.<br><br>" + str(response.json())
        except requests.exceptions.ConnectionError as e:
            return "API inaccessible. Please try again later.<br><br>" + str(e)

        if response.json()["data"] == 1:
            return "User already exists. Please try again with a different username."
        else:
            request_data = {
                "username": username,
                "email": email,
                "password": password
            }

            try:
                response = requests.post(f"{API_BASEURL}/post/new-jiujitsu-user", headers=HEADERS, json=request_data)
                try:
                    response.json()
                except requests.exceptions.JSONDecodeError as e:
                    return "API response error. Please try again later.<br><br>" + str(response) + "<br><br>" + str(e)
                if response.json()["result"] == "failed":
                    if response.json()["error"] == "Unauthorized":
                        return "Unauthorized. Please try again later.<br><br>" + str(response.json())
                    else:
                        return "API error. Please try again later.<br><br>" + str(response.json())
            except requests.exceptions.ConnectionError as e:
                return "API inaccessible. Please try again later.<br><br>" + str(e)
            else:
                return "User registered successfully. Please login to continue."

    return render_template("main/login-register.html", title=" SMRJJ Register", page="register")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5022)
