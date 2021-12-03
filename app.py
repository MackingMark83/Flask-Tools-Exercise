from flask import Flask,request, render_template, redirect, flash  
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecret"
debug = DebugToolbarExtension(app)


responses = []



@app.route("/")
def show_survey_start():
    """Select a survey."""

    return render_template("survey_start.html", survey=survey)
