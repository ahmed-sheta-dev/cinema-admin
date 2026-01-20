from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.models import Booking, Showtime


def get_showtime_with_hall(db: Session, showtime_id: int) -> Showtime | None:
    stmt = select(Showtime).where(Showtime.id == showtime_id)
    return db.execute(stmt).scalar_one_or_none()


def total_booked_seats(db: Session, showtime_id: int) -> int:
    stmt = select(func.count(Booking.id)).where(
        Booking.showtime_id == showtime_id, Booking.status == "confirmed"
    )
    return db.execute(stmt).scalar_one_or_none()


def create_booking(db: Session, booking: Booking) -> Booking:
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def list_bookings(db: Session) -> list[Booking]:
    stmt = select(Booking).order_by(Booking.id.desc())
    return list(db.execute(stmt).scalars().all())
