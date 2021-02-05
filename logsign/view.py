from views.pythondb import init_bp
from flask import render_template, request, redirect, url_for
# session and database support
from flask_login import login_required
from models import login_manager
from models.lessons import menus
from models.crud import model_create, model_read, model_update, model_delete, model_query_all, model_query_emails, \
    model_query_phones
from models.login import model_authorize, model_login, model_logout


# connects default URL to a function
@app.route('/')
def databases():
    """convert Users table into a list of dictionary rows"""
    records = model_query_all()
    return render_template("pythondb/index.html", table=records, menus=menus)


# create/add a new record to the table
@app.route('/create/', methods=["POST"])
def create():
    if request.form:
        """extract data from form"""
        user_dict = {'username': request.form.get("username"), 'password': request.form.get("password"),
                     'email': request.form.get("email"), 'phone_number': request.form.get("phone_number")}
        # model_create expects: username, password, email, phone_number
        model_create(user_dict)
    return redirect(url_for('pythondb_bp.databases'))



# Authorise User Section
# if auth user is the signup section
# the public page does not include @login_required
@app.route('/public/')
def public():
    return render_template("pythondb/public_page.html")


@app.route('/auth_user/', methods=["GET", "POST"])
def auth_user():
    # check form inputs and create auth user
    if request.form:
        # validation should be in HTML
        user_dict = {
            'user_name': request.form.get("txtUsername"),
            'email': request.form.get("txtEmail"),
            'password': request.form.get("txtPwd1")
        }
        # model_authorize requires user_dict: user_name, email, password
        model_authorize(user_dict)
        return redirect(url_for('pythondb_bp.login'))
    # show the auth user page if the above fails for some reason
    return render_template("pythondb/auth_user.html")


# if login url, show phones table only
@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.form:
        # validation should be in HTML
        user_dict = {
            'user_name': request.form.get("txtUsername"),
            'email': request.form.get("txtEmail"),
            'password': request.form.get("txtPwd1")
        }
        if model_login(user_dict):
            return redirect(url_for('pythondb_bp.dashboard'))

    # if not logged in, show the login page
    return render_template("pythondb/login.html")


# logged in users can see the dashboard
@app.route('/dashboard/')
@login_required  # this is the code that Flask-Login uses to stop non logged in users
def dashboard():
    return render_template("pythondb/dashboard.html")


# give users a way to log out
@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    model_logout()
    return redirect(url_for('pythondb_bp.login'))


# this code lets Flask-Login take unauthorised users back to the login page
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('pythondb_bp.login'))