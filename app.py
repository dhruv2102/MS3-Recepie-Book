import os
from flask import (Flask, flash, render_template,
                  redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # Logic for existing user
        if existing_user:
            flash("Username already exists, try again")
            return redirect('sign_up')

        # Adding New User
        new_user = {
            "name": request.form.get("name"),
            "username":  request.form.get('username').lower(),
            "password": generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(new_user)

        # Adding session cookie
        session['user'] = request.form.get("username").lower()
        flash('You are sucessfully signed up!!!')

        # Redirect to Profile Page------------------------------------------ 
        # Need to do
    return render_template('sign_up.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
    
        if existing_user:
            entered_password = request.form.get("password")
            user_password = existing_user["password"]
            users_name = existing_user['name']

            if check_password_hash(entered_password, user_password):
                session["user"] = existing_user['username']
                flash("Welcome {}".format(users_name))
                # Redirect to profile
                return redirect(url_for('get_recepies'))
            else:
                flash("Your username/password was wrong")
                return redirect(url_for('login'))
        else:
            flash("User doesn't exist, please sign up")
            return redirect(url_for('sign_up'))
    
    return render_template('login.html')


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


@app.route('/logout')
def logout():
    # Remove user from sesion cookie
    session.pop('user')
    return redirect(url_for('home')) 


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), 
            debug=True)