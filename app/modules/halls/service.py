from sqlalchemy.orm import Session

from app.db.models.hall import Hall
from app.modules.halls.repo import create_hall, list_halls
from app.modules.halls.schemas import HallCreate, HallOut


def get_halls(db: Session) -> list[HallOut]:
    halls = list_halls(db)
    return [
        HallOut(
            id=h.id,
            name=h.name,
            capacity=h.capacity,
            created_at=h.created_at,
        )
        for h in halls
    ]


def add_hall(db: Session, payload: HallCreate) -> HallOut:
    new_hall = Hall(
        name=payload.name,
        capacity=payload.capacity,
    )
    created_hall = create_hall(db, new_hall)
    return HallOut(
        id=created_hall.id,
        name=created_hall.name,
        capacity=created_hall.capacity,
    )
