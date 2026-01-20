from sqlalchemy.orm import Session

from app.db.models import Booking
from app.modules.bookings.repo import (
    create_booking,
    get_showtime_with_hall,
    list_bookings,
    total_booked_seats,
)
from app.modules.bookings.schemas import BookingCreate, BookingOut


def get_bookings(db: Session) -> list[BookingOut]:
    bookings = list_bookings(db)
    return [
        BookingOut(
            id=b.id,
            showtime_id=b.showtime_id,
            customer_name=b.customer_name,
            customer_phone=b.customer_phone,
            seats=b.seats,
            status=b.status,
        )
        for b in bookings
    ]


def add_booking(db: Session, payload: BookingCreate) -> BookingOut:
    # Check showtime existence
    showtime = get_showtime_with_hall(db, payload.showtime_id)
    if not showtime:
        raise ValueError("showtime_not_found")

    hall = showtime.hall
    if hall is None:
        raise ValueError("hall_not_found")

    # Check seat availability
    booked_seats = total_booked_seats(db, payload.showtime_id)
    available_seats = hall.capacity - booked_seats
    if payload.seats > available_seats:
        raise ValueError("not_enough_seats")

    booking = Booking(
        showtime_id=payload.showtime_id,
        customer_name=payload.customer_name,
        customer_phone=payload.customer_phone,
        seats=payload.seats,
    )
    booking = create_booking(db, booking)

    return BookingOut(
        id=booking.id,
        showtime_id=booking.showtime_id,
        customer_name=booking.customer_name,
        customer_phone=booking.customer_phone,
        seats=booking.seats,
        status=booking.status,
    )
