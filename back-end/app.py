#!/usr/bin/env python3
"""Entry point of app"""

from flask import abort, Flask, jsonify, redirect, request
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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """POST /sessions route for user login."""
    username = request.form.get("username")
    password = request.form.get("password")

    if not AUTH.valid_login(username, password):
        abort(401)  # Unauthorized access

    session_id = AUTH.create_session(username)
    response = jsonify({"username": username, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """DELETE /sessions route for logging out."""
    # Retrieve session_id from the cookie
    session_id = request.cookies.get("session_id")
    if session_id is None:
        return abort(403)

    # Find the user with the session_id
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        return abort(403)

    # Destroy the session and redirect to home page
    AUTH.destroy_session(user.id)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
