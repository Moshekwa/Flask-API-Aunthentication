import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("stores", __name__, description="GET Request Operations")

@blp.route("/")
class Home(MethodView):
    def get(self):
        try:
            return {"Message":"Welcome to Flask API Authentication Project"}
        except Exception as e:
            return e, 500