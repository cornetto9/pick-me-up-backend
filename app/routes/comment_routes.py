from flask import Blueprint, request, jsonify
from app.models.comment import Comment
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