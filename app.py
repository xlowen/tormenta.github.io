import os

from cs50 import SQL
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///spells.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/divina", methods=["GET", "POST"])
def divine():
    """Divine spells list"""

    dmagias = db.execute(
        "SELECT * FROM divine JOIN ddesc ON ddesc.ddesc_id = divine.id")

    if request.method == "POST":
        usrflt = request.form.get("filter")
        usrfltn = request.form.get("sname")

        if not usrflt and not usrfltn:
            dmagias = db.execute(
                "SELECT * FROM divine JOIN ddesc ON ddesc.ddesc_id = divine.id")
            return render_template("divine.html", dmagias=dmagias)

        if not usrflt:

            dmagias = db.execute(
                "SELECT * FROM divine JOIN ddesc ON ddesc.ddesc_id = divine.id WHERE dspell LIKE ? OR fdesc LIKE ? ORDER BY dcircle", "%" + usrfltn + "%", "%" + usrfltn + "%")
            return render_template("divina.html", dmagias=dmagias)

        if usrflt.isnumeric():

            dmagias = db.execute(
                "SELECT * FROM divine JOIN ddesc ON ddesc.ddesc_id = divine.id WHERE dcircle = ? ORDER BY dcircle", usrflt)
            return render_template("divina.html", dmagias=dmagias)

    return render_template("divina.html", dmagias=dmagias)


@app.route("/arcana", methods=["GET", "POST"])
def arcane():
    """Arcane spells list"""

    amagias = db.execute(
        "SELECT * FROM arcane JOIN adesc ON adesc.adesc_id = arcane.id")

    if request.method == "POST":
        usrflt = request.form.get("filter")
        usrfltn = request.form.get("sname")

        if not usrflt and not usrfltn:
            amagias = db.execute(
                "SELECT * FROM arcane JOIN adesc ON adesc.adesc_id = arcane.id")
            return render_template("arcana.html", amagias=amagias)

        if not usrflt:

            amagias = db.execute(
                "SELECT * FROM arcane JOIN adesc ON adesc.adesc_id = arcane.id WHERE aspell LIKE ? OR fdesc LIKE ? ORDER BY acircle", "%" + usrfltn + "%", "%" + usrfltn + "%")
            return render_template("arcana.html", amagias=amagias)

        if usrflt.isnumeric():

            amagias = db.execute(
                "SELECT * FROM arcane JOIN adesc ON adesc.adesc_id = arcane.id WHERE acircle = ? ORDER BY acircle", usrflt)
            return render_template("arcana.html", amagias=amagias)

    return render_template("arcana.html", amagias=amagias)


@app.route("/ogl", methods=["GET"])
def ogl():

    return render_template("ogl.html")


@app.route("/cs50", methods=["GET"])
def cs50():

    return render_template("cs50.html")
