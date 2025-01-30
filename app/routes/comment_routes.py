from flask import Blueprint, request
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