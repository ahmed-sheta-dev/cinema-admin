from sqlalchemy.orm import Session

from app.db.models.showtime import Showtime
from app.modules.showtimes.repo import create_showtime, list_showtimes
from app.modules.showtimes.schemas import ShowtimeCreate, ShowtimeOut


def get_showtimes(db: Session) -> list[ShowtimeOut]:
    showtimes = list_showtimes(db)
    return [
        ShowtimeOut(
            id=s.id,
            movie_id=s.movie_id,
            hall_id=s.hall_id,
            starts_at=s.starts_at,
            price=float(s.price),
            status=s.status,
        )
        for s in showtimes
    ]


def add_showtime(db: Session, payload: ShowtimeCreate) -> ShowtimeOut:
    new_showtime = Showtime(
        movie_id=payload.movie_id,
        hall_id=payload.hall_id,
        starts_at=payload.starts_at,
        price=payload.price,
        status=payload.status,
    )
    created_showtime = create_showtime(db, new_showtime)
    return ShowtimeOut(
        id=created_showtime.id,
        movie_id=created_showtime.movie_id,
        hall_id=created_showtime.hall_id,
        starts_at=created_showtime.starts_at,
        price=float(created_showtime.price),
        status=created_showtime.status,
    )
