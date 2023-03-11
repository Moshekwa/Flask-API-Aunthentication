from functools import wraps
from flask import request, jsonify

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')

        # Check if token is valid here (e.g., look it up in a database)
        if not is_valid_token(token):
            return jsonify({'message': 'Invalid token'}), 401

        return func(*args, **kwargs)

    return wrapper

@app.route('/protected/')
@authenticate
def protected_endpoint():
    return jsonify({'message': 'You are authenticated!'})
