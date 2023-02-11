from app import app
from flask import request, redirect, url_for
from .models import User, Candy
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash


@app.route('/')
def homePage():
    return {
        "test": "hi"
    }

@app.route('/api', methods=["GET", "POST"])
def api():
    return {
        "response": "ok",
        "message": "Future API page"
    }