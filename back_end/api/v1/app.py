from back_end.api.v1 import create_app
from flask import jsonify

app = create_app({'DEVELOPMENT': True})


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """GET route to return homepage."""
    return jsonify({"message": "Bienvenue!"})


if __name__ == '__main__':
    app.run(debug=True)
