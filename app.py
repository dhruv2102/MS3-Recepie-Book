import os
import requests
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

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
    return render_template("home.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        # Logic for existing user
        if existing_user:
            flash("Username already exists, try again")
            return redirect("sign_up")

        # Adding New User
        new_user = {
            "name": request.form.get("name"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(new_user)

        # Adding session cookie
        session["user"] = request.form.get("username").lower()
        flash("You are sucessfully signed up!!!")

        # Redirect to Profile Page
        return redirect(url_for('profile', username=session['user']))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            entered_password = request.form.get("password")
            user_password = existing_user["password"]
            users_name = existing_user["name"]
            username = existing_user["username"]

            if check_password_hash(user_password, entered_password):
                session["user"] = existing_user["username"]
                flash("Welcome {}".format(users_name))

                return redirect(url_for("profile", username=username))
            else:
                flash("Your username/password was wrong")
                return redirect(url_for("login"))

        else:
            flash("User doesn't exist, please sign up")
            return redirect(url_for("sign_up"))

    return render_template("login.html")


@app.route("/get_recepies")
def get_recepies():
    recepies = list(mongo.db.recepies.find())
    return render_template("recepies.html", recepies=recepies)


@app.route("/get_individual_recepie/<recepie_id>")
def get_individual_recepie(recepie_id):
    recepie = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    return render_template("individual_recepie.html", recepie=recepie)


@app.route("/logout")
def logout():
    # Remove user from sesion cookie
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/profile/<username>")
def profile(username):
    # If session user is not same as logged in user then
    # log then empty the session user string
    if session['user'] == username:
        existing_user = mongo.db.users.find_one({"username": username})
        users_name = existing_user["name"]
        recepies = list(mongo.db.recepies.find({"created_by": username}))
        # Getting all recipes for admin
        if session['user'] == "admin":
            recepies = list(mongo.db.recepies.find())
        return render_template(
            "profile.html", users_name=users_name, recepie_list=recepies)
    flash('Wrong profile, please log in again')
    session.pop('user')
    return redirect(url_for("login"))


@app.route("/add_recepie", methods=['GET', 'POST'])
def add_recepie():
    if session.get('user') is None:
        flash('Please Sign In')
        return redirect(url_for('login'))

    if request.method == 'POST':
        image_url = request.form.get("image_url")
        if is_url_image(image_url):
            final_url = image_url
        else:
            temp = (
                'https://image.freepik.com/free-photo/wooden-',
                'background-with-basket-full-vegetables_23-2147609629.jpg'
            )
            final_url = temp[0] + temp[1]

        recepie = {
            "recepie_name": request.form.get("recepie_name"),
            "category_name": request.form.get("category_name"),
            "ingredients": request.form.get("ingredients"),
            "image_url": final_url,
            "Servings": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "steps": request.form.get("instructions"),
            "Tips": request.form.get("tips"),
            "created_by": session['user'],
            "comments": [],
        }
        mongo.db.recepies.insert_one(recepie)
        flash("Recipe added")
        return redirect(url_for('profile', username=session['user']))

    categories = list(mongo.db.categories.find())
    return render_template('add_recepie.html', categories=categories)


@app.route("/edit_recepie/<recepie_id>", methods=['GET', 'POST'])
def edit_recepie(recepie_id):
    if session.get('user') is None:
        flash('Please Sign In')
        return redirect(url_for('login'))

    if request.method == 'POST':
        recepie = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
        edited_recepie = {
            "recepie_name": request.form.get("recepie_name"),
            "category_name": request.form.get("category_name"),
            "ingredients": request.form.get("ingredients"),
            "image_url": request.form.get("image_url"),
            "Servings": request.form.get("serves"),
            "prep_time": request.form.get("prep_time"),
            "steps": request.form.get("instructions"),
            "Tips": request.form.get("tips"),
            "created_by": session['user'],
            "comments": recepie['comments'],
        }
        mongo.db.recepies.update({"_id": ObjectId(recepie_id)}, edited_recepie)
        flash("Recipe added")
        return redirect(url_for('profile', username=session['user']))

    recepie = mongo.db.recepies.find_one({"_id": ObjectId(recepie_id)})
    categories = list(mongo.db.categories.find())
    return render_template(
        'edit_recepie.html', categories=categories, recepie=recepie)


@app.route("/delete_recepie/<recepie_id>")
def delete_recepie(recepie_id):
    if session.get('user') is None:
        flash('Please Sign In')
        return redirect(url_for('login'))

    mongo.db.recepies.remove({"_id": ObjectId(recepie_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for('profile', username=session['user']))


@app.route("/categories")
def categories():
    if session.get('user') is None:
        flash('Please Sign In')
        return redirect(url_for('login'))

    if session['user'] == 'admin':
        all_categories = mongo.db.categories.find()
        return render_template('categories.html', categories=all_categories)

    session.pop('user')
    return redirect(url_for('login'))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if session.get('user') is None:
        flash('Please Sign In')
        return redirect(url_for('login'))

    if session['user'] == 'admin':
        if request.method == 'POST':
            new_category = {
                "category_name": request.form.get("category_name"),
            }
            mongo.db.categories.insert_one(new_category)
            flash("Category added")
            return redirect(url_for('categories'))
        return render_template('add_category.html')

    session.pop('user')
    return redirect(url_for('login'))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if session.get('user') is None:
        flash('Please Sign In')
        return redirect(url_for('login'))

    if session['user'] == 'admin':
        if request.method == 'POST':
            edited_category = {
                "category_name": request.form.get("category_name"),
            }
            mongo.db.categories.update(
                {"_id": ObjectId(category_id)}, edited_category
            )
            flash("Category updated")
            return redirect(url_for('categories'))
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template('edit_category.html', category=category)

    session.pop('user')
    return redirect(url_for('login'))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    if session.get('user') is None:
        flash('Please Sign In')
        return redirect(url_for('login'))

    if session['user'] == 'admin':
        category = mongo.db.categories.find_one(
            {"_id": ObjectId(category_id)}
        )
        category_name = category['category_name']

        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category successfully deleted")

        recipes = list(mongo.db.recepies.find({
            'category_name': category_name
        }))

        for item in recipes:
            _id = item['_id']
            mongo.db.recepies.remove({"_id": ObjectId(_id)})
    # Remove the recepies with the given category
        return redirect(url_for('categories'))

    session.pop('user')
    return redirect(url_for('login'))


# https://docs.mongodb.com/manual/text-search/ - Searching for text
@app.route('/search_bar', methods=["GET", "POST"])
def search_bar():
    searched_text = request.form.get("search_bar")
    # https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search
    mongo.db.recepies.drop_indexes()
    mongo.db.recepies.create_index([("$**", 'text')])

    cursor = (mongo.db.recepies.find(
        {"$text": {"$search": searched_text}})
        )

    # https://code-institute-room.slack.com/files/UD62BF5GC/FJVAS8C0H/-.pl
    recepies = []

    for i in cursor:
        recepies.append(i)

    if recepies == []:
        flash('No recipes found')
        return redirect('get_recepies')

    return render_template("recepies.html", recepies=recepies)


@app.route('/delete_comment/<recepie_id>/<loop_index>')
def delete_comment(recepie_id, loop_index):
    recepie = mongo.db.recepies.find_one({
        "_id": ObjectId(recepie_id)
    })
    comments = recepie['comments']
    comments.pop(int(loop_index)-1)
    recepie['comments'] = comments
    mongo.db.recepies.update({"_id": ObjectId(recepie_id)}, recepie)
    return redirect(url_for('get_individual_recepie', recepie_id=recepie_id))


@app.route('/add_comment/<recepie_id>', methods=["GET", "POST"])
def add_comment(recepie_id):
    if request.method == 'POST':
        recepie = mongo.db.recepies.find_one({
            "_id": ObjectId(recepie_id)
        })
        comments = recepie['comments']

        user_comment = request.form.get('comment')
        currect_user = session['user']
        timestamp = datetime.now()

        _tuple = (currect_user, timestamp, user_comment)
        comments.append(_tuple)
        recepie['comments'] = comments
        mongo.db.recepies.update({"_id": ObjectId(recepie_id)}, recepie)
    return redirect(url_for('get_individual_recepie', recepie_id=recepie_id))


@app.route('/edit_comment/<recepie_id>/<loop_index>', methods=["GET", "POST"])
def edit_comment(recepie_id, loop_index):
    recepie = mongo.db.recepies.find_one(
        {"_id": ObjectId(recepie_id)}
    )
    comment_list = recepie['comments']
    comment = comment_list[int(loop_index)-1]
    if request.method == "POST":
        updated_comment = request.form.get('comment')
        comment[1] = datetime.now()
        comment[2] = updated_comment
        comment_list[int(loop_index)-1] = comment
        recepie['comments'] = comment_list
        mongo.db.recepies.update({"_id": ObjectId(recepie_id)}, recepie)
        return redirect(
            url_for("get_individual_recepie", recepie_id=recepie_id)
            )

    return render_template('edit_comment.html', comment=comment)


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        user_email = request.form.get('email')
        email_doc = {
            "email": user_email,
        }
        mongo.db.subscribed_user.insert_one(email_doc)
        flash('You are subscribed')
    return redirect(url_for('home'))


# https://stackoverflow.com/questions/10543940/check-if-a-url-to-an-image-is-up-and-exists-in-python
def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return True
    return False


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"), port=int(os.environ.get("PORT")), 
        debug=False
    )
