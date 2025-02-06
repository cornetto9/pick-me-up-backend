from flask import Blueprint, request, jsonify
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

# Endpoint to fetch items posted by the user
@bp.get("/user/<int:user_id>")
def get_user_items(user_id):
    items = Item.query.filter_by(user_id=user_id).all()
    return jsonify([item.to_dict() for item in items]), 200

# Endpoint to update the availability status of an item
@bp.patch("/<int:id>")
def update_item_status(id):
    request_body = request.get_json()
    availability = request_body.get("availability")
    user_id = request.args.get("user_id")
    if user_id is None:
        return jsonify({"error": "User ID is required"}), 400

    item = Item.query.get(id)
    if item and item.user_id == int(user_id):
        item.availability = availability
        db.session.commit()
        return jsonify(item.to_dict()), 200
    return jsonify({"error": "Item not found or user not authorized"}), 404

# Endpoint to delete an item by its ID
@bp.delete("/<int:item_id>")
def delete_item(item_id):
    user_id = request.args.get("user_id")
    if user_id is None:
        return jsonify({"error": "User ID is required"}), 400

    item = Item.query.get(item_id)
    if item and item.user_id == int(user_id):
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item deleted successfully"}), 200
    return jsonify({"error": "Item not found or user not authorized"}), 404

# Endpoint to delete all items
@bp.delete("/all")
def delete_all_items():
    db.session.query(Item).delete()
    db.session.commit()
    return jsonify({"message": "All items deleted successfully"}), 200