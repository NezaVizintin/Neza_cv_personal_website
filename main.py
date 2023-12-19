from flask import Flask, render_template
import json
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", classes_cards="card col-12 col-xl p-0 d-flex")


@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("hair_salon_index.html")


@app.route("/fact-generator")
def fact_generator():
    with open("facts.json", "r") as facts_file:  # opens score file to read
        fact_list = json.loads(facts_file.read())

    fact = random.choice(list(fact_list.values()))

    return fact


if __name__ == "__main__":
    app.run(use_reloader=True)
