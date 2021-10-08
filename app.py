import os
from flask import (Flask, flash, render_template,
                  redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env


# ----------------------- Connectiong to Flask
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists, try again")
            return redirect('sign_up')
    return render_template('sign_up.html')


@app.route("/get_recepies")
def get_recepies():
    recepies = list(mongo.db.recepies.find())
    return render_template('recepies.html', recepies=recepies)


@app.route("/get_individual_recepie/<recepie_id>")
def get_individual_recepie(recepie_id):
    recepie = mongo.db.recepies.find_one(
        {
            "_id": ObjectId(recepie_id)
        }
    )
    return render_template("individual_recepie.html", recepie=recepie)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), 
            debug=True)