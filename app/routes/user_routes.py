from flask import Blueprint, request, jsonify
from app.models.user import User
from app.db import db
from .routes_utilities import get_models_with_filters

bp = Blueprint("user_bp", __name__, url_prefix="/users")

@bp.get("")
def get_all_users():
    return get_models_with_filters(User, request.args)

# Endpoint to fetch the current user's data
@bp.get("/<int:user_id>")
def get_current_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

# Endpoint to update a user's information
@bp.patch("/<int:user_id>")
def update_user(user_id):
    request_user_id = request.args.get("user_id")
    if request_user_id is None or int(request_user_id) != user_id:
        return jsonify({"error": "User ID is required or not authorized"}), 400

    request_body = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.email = request_body.get("email", user.email)
        user.username = request_body.get("username", user.username)
        if "password" in request_body:
            user.password_hash = user.generate_password_hash(request_body["password"])
        db.session.commit()
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

# Endpoint to delete a user by their ID
@bp.delete("/<int:user_id>")
def delete_user(user_id):
    request_user_id = request.args.get("user_id")
    if request_user_id is None or int(request_user_id) != user_id:
        return jsonify({"error": "User ID is required or not authorized"}), 400

    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404