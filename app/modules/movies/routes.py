from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.db.session import get_db
from app.modules.movies.schemas import MovieCreate
from app.modules.movies.service import add_movie, get_movies

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")


@movies_bp.route("/", methods=["GET"])
def list_all_movies():
    db = get_db()
    movies = get_movies(db)
    return jsonify([movie.model_dump() for movie in movies]), 200


@movies_bp.route("/", methods=["POST"])
def create_movie():
    try:
        payload = MovieCreate.model_validate(request.get_json(force=True))
    except ValidationError as e:
        return jsonify({"error": "Invalid input", "details": e.errors()}), 400

    db = get_db()
    new_movie = add_movie(db, payload)
    return jsonify(new_movie.model_dump()), 201
