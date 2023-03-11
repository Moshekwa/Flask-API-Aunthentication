from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from functools import wraps

from CONFIG import key

blp = Blueprint("Get Requests Routes", __name__, description="GET Request Operations")

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('token')

        if token != key:
            return {"message":"Unauthorized access"},401
        else:
            return func(*args, **kwargs)

    return wrapper

@blp.route("/")
class Home(MethodView):
    @authenticate
    def get(self):
        try:
            return {"Message":"Your are authenticated! :)"}
        except Exception as e:
            return e, 500