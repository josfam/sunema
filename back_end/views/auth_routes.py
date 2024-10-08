from back_end.views import app_views
from flask import request, jsonify, abort, redirect
from back_end.utils.auth import Auth
from sqlalchemy.orm.exc import NoResultFound

"""
FIX: Normalize usernames to lowercase to prevent duplicate entries 
with different cases (e.g., 'grace' and 'Grace')
"""

AUTH = Auth()

@app_views.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """POST /sessions route for user login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not AUTH.valid_login(username, password):
        abort(401)  # Unauthorized access
    try:
        session_id = AUTH.create_session(username)
        response = jsonify({"username": username, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    except (ValueError, NoResultFound):
        return jsonify({"message": "Error while logging in"}), 500


@app_views.route("/sessions", methods=["DELETE"], strict_slashes=False)
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


@app_views.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """POST /users route for registering a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        user = AUTH.register_user(username, password)
        return (
            jsonify({"username": user.username, "message": "user created"}),
            200,
        )
    except ValueError:
        abort(401)

@app_views.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """GET /profile route to get user profile using session_id cookie."""
    session_id = request.cookies.get("session_id")
    if session_id is None:
        return abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        return abort(403)

    # Return the user's email in the response
    return jsonify({"email": user.email}), 200
