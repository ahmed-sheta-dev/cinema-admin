from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from app.db.session import get_db
from app.modules.showtimes.schemas import ShowtimeCreate
from app.modules.showtimes.service import add_showtime, get_showtimes

showtimes_bp = Blueprint("showtimes", __name__, url_prefix="/showtimes")


@showtimes_bp.route("/", methods=["GET"])
def list_all_showtimes():
    db = get_db()
    showtimes = get_showtimes(db)
    return jsonify([st.model_dump() for st in showtimes]), 200


@showtimes_bp.route("/", methods=["POST"])
def create_new_showtime():
    try:
        payload = ShowtimeCreate.model_validate(request.json)
    except ValidationError as e:
        return jsonify({"error": "Invalid input", "details": e.errors()}), 400

    db = get_db()
    try:
        new_showtime = add_showtime(db, payload)
    except IntegrityError as e:
        db.rollback()
        return jsonify({"error": "invalid_movie_or_hall_id", "details": str(e)}), 400

    return jsonify(new_showtime.model_dump()), 201
