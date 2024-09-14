#!/usr/bin/env python3
"""Entry point of app"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """GET route to return homepage."""
    return jsonify({"message": "Bienvenue!"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """POST /users route for registering a new user."""
    username = request.form.get("username")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(username, password)
        return jsonify({"username": user.username, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "username already registered"}), 400


if __name__ == '__main__':
    app.run(debug=True)
