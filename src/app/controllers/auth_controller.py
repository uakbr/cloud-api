# src/app/controllers/auth_controller.py

from flask import Blueprint, request, jsonify, make_response
from flask_login import login_user, logout_user, login_required
from ..models.user import User
from ..app import db
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from ..config import Config

config = Config()

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return make_response('Missing fields', 400)

    user = User.query.filter_by(username=username).first()

    if user:
        return make_response('Username already exists', 400)

    user = User.query.filter_by(email=email).first()

    if user:
        return make_response('Email already exists', 400)

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return make_response('User created', 201)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return make_response('Missing fields', 400)

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return make_response('Invalid credentials', 401)

    login_user(user)

    s = Serializer(config.SECRET_KEY, 60 * 60 * 24)
    token = s.dumps({'id': user.id}).decode('utf-8')

    return jsonify({'token': token})

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return make_response('Logged out', 200)