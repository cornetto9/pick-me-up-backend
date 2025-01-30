from flask import abort, make_response, request
from ..db import db
# from ..models.user import User
# from ..models.item import Item
# from ..models.comment import Comment

def create_model(cls, model_data): 
    try: 
        new_model = cls.from_dict(model_data) 
    except KeyError as error: 
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))        
    db.session.add(new_model) 
    db.session.commit()
    return make_response({f"{cls.__name__.lower()}": new_model.to_dict()}, 201)


def get_models_with_filters(cls, filters): 
    query = db.select(cls)
    for key, value in filters.items():
        query = query.where(getattr(cls, key) == value)
    models = db.session.execute(query).scalars().all()
    return make_response({f"{cls.__name__.lower()}": [model.to_dict() for model in models]}, 200)

def validate_user_data(data):
    if 'email' not in data or 'password' not in data:
        response = {"details": "Invalid data"}
        abort(make_response(response, 400))