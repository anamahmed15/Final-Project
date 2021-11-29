from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import utility

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)
outputpath = "recording.wav"


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/record")
def record():

    utility.record()

    return render_template("index.html")


@app.route("/analyze")
def analyze():
    result, certainty = utility.perform_analysis(outputpath)
    return render_template("index.html", result=result, certainty=certainty)


if __name__ == "__main__":
    app.run()
