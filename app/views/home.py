from flask import Blueprint, render_template

#from flask_login import login_required

home = Blueprint('home', __name__)


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html')


@home.route('/dashboard')
#@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html')