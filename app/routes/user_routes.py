from flask import Blueprint, request
from app.models.user import User
from .routes_utilities import create_model, get_models_with_filters
from app.db import db
import requests
import os

bp = Blueprint("user_bp", __name__, url_prefix="/users")

@bp.post("")
def create_board():
    request_body = request.get_json()
    return create_model(User,request_body)

@bp.get("")
def get_all_users():
    return get_models_with_filters(User, request.args)