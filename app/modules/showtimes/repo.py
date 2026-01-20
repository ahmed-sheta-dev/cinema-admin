from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.showtime import Showtime


def list_showtimes(db: Session) -> list[Showtime]:
    stmt = select(Showtime).order_by(Showtime.id.desc())
    return list(db.execute(stmt).scalars().all())


def create_showtime(db: Session, showtime: Showtime) -> Showtime:
    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime
