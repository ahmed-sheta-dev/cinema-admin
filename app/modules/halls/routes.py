from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from app.db.session import get_db
from app.modules.halls.schemas import HallCreate
from app.modules.halls.service import add_hall, get_halls

halls_bp = Blueprint("halls", __name__, url_prefix="/halls")


@halls_bp.route("/", methods=["GET"])
def list_all_halls():
    db = get_db()
    halls = get_halls(db)
    return jsonify([hall.model_dump() for hall in halls]), 200


@halls_bp.route("/", methods=["POST"])
def create_hall():
    try:
        payload = HallCreate.model_validate(request.get_json(force=True))
    except ValidationError as e:
        return jsonify({"error": "Invalid input", "details": e.errors()}), 400

    db = get_db()
    try:
        new_hall = add_hall(db, payload)
    except IntegrityError as e:
        return jsonify({"error": "hall_name_already_exists", "details": str(e)}), 409

    return jsonify(new_hall.model_dump()), 201
