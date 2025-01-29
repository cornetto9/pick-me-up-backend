from flask import Blueprint, request, jsonify
from app.models.user import User
from ..db import db
from .routes_utilities import validate_user_data

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
        return jsonify({'error':'Invalid email or password'})