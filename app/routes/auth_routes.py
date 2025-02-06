from flask import Blueprint, request, jsonify
from app.models.user import User
from ..db import db
from .routes_utilities import validate_user_data
from flask_bcrypt import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    validate_user_data(data)

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.verify_password(password):
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    validate_user_data(data)

    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
        return jsonify({'error': 'Email or username already exists'}), 400

    password_hash = generate_password_hash(password).decode('utf8')

    new_user = User(
        email=email,
        username=username,
        password_hash=password_hash
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201