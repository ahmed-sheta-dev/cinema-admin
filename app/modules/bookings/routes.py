from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from app.db.session import get_db
from app.modules.bookings.schemas import BookingCreate
from app.modules.bookings.service import add_booking, get_bookings

bookings_bp = Blueprint("bookings", __name__, url_prefix="/bookings")


@bookings_bp.route("/", methods=["POST"])
def create_new_booking():
    try:
        payload = BookingCreate.model_validate(request.get_json(force=True))
    except ValidationError as e:
        return jsonify({"error": "validation_error", "details": e.errors()}), 422

    db = get_db()
    try:
        booking = add_booking(db, payload)
    except ValueError as e:
        msg = str(e)
        if msg == "showtime_not_found":
            return jsonify({"error": "showtime_not_found"}), 404
        if msg == "not_enough_seats":
            return jsonify({"error": "not_enough_seats"}), 409
        return jsonify({"error": "bad_request"}), 400

    return jsonify(booking.model_dump()), 201


@bookings_bp.route("/", methods=["GET"])
def list_all_bookings():
    db = get_db()
    bookings = get_bookings(db)
    return jsonify([b.model_dump() for b in bookings]), 200
