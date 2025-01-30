from flask import Blueprint, request
from app.models.item import Item
from .routes_utilities import create_model, get_models_with_filters
from app.db import db

bp = Blueprint("item_bp", __name__, url_prefix="/items")

@bp.post("")
def create_item():
    request_body = request.get_json()
    return create_model(Item, request_body)

@bp.get("")
def get_all_items():
    return get_models_with_filters(Item, request.args)