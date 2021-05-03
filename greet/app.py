from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "welcome"


@app.route('/welcome/<greeting>')
def welcome_greet(greeting):
    return f"welcome {greeting}"
