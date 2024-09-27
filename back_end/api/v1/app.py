from back_end.api.v1 import create_app
from flask import jsonify
from back_end.models.samples.sample_utils import (
    sample_films_exist,
    save_films_to_db,
    sample_collections)

app = create_app({'DEVELOPMENT': True})

# populate the sample database with films
with app.app_context():
    if not sample_films_exist():
        save_films_to_db(sample_collections)

@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """GET route to return homepage."""
    return jsonify({"message": "Bienvenue!"})


if __name__ == '__main__':
    app.run(debug=True)
