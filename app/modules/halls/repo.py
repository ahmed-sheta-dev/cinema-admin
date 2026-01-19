from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.hall import Hall


def list_halls(db: Session) -> list[Hall]:
    stmt = select(Hall).order_by(Hall.id.desc())
    return list(db.execute(stmt).scalars().all())


def create_hall(db: Session, hall: Hall) -> Hall:
    db.add(hall)
    db.commit()
    db.refresh(hall)
    return hall
