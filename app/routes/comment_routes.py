from flask import Blueprint, request, jsonify
from app.models.comment import Comment
from app.models.user import User
from .routes_utilities import create_model, get_models_with_filters
from app.db import db

bp = Blueprint("comment_bp", __name__, url_prefix="/comments")

@bp.post("")
def create_comment():
    request_body = request.get_json()
    return create_model(Comment, request_body)

@bp.get("")
def get_all_comments():
    return get_models_with_filters(Comment, request.args)

# Endpoint to update a comment by its ID
@bp.patch("/<int:comment_id>")
def update_comment(comment_id):
    request_body = request.get_json()
    comment_text = request_body.get("comment_text")
    user_id = request.args.get("user_id")
    if user_id is None:
        return jsonify({"error": "User ID is required"}), 400

    comment = Comment.query.get(comment_id)
    if comment and comment.user_id == int(user_id):
        comment.comment_text = comment_text
        db.session.commit()
        return jsonify(comment.to_dict()), 200
    return jsonify({"error": "Comment not found or user not authorized"}), 404

# Endpoint to delete a comment by its ID
@bp.delete("/<int:comment_id>")
def delete_comment(comment_id):
    user_id = request.args.get("user_id")
    if user_id is None:
        return jsonify({"error": "User ID is required"}), 400

    comment = Comment.query.get(comment_id)
    if comment and comment.user_id == int(user_id):
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"message": "Comment deleted successfully"}), 200
    return jsonify({"error": "Comment not found or user not authorized"}), 404

# Endpoint to get all comments from a specific user
@bp.get("/user/<int:user_id>")
def get_user_comments(user_id):
    comments = Comment.query.filter_by(user_id=user_id).all()
    return jsonify([comment.to_dict() for comment in comments]), 200

# Endpoint to delete all comments from a specific user
@bp.delete("/user/<int:user_id>")
def delete_user_comments(user_id):
    request_user_id = request.args.get("user_id")
    if request_user_id is None or int(request_user_id) != user_id:
        return jsonify({"error": "User ID is required or not authorized"}), 400

    comments = Comment.query.filter_by(user_id=user_id).all()
    for comment in comments:
        db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "All comments from user deleted successfully"}), 200