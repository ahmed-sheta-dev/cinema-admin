from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.movie import Movie


def list_movies(db: Session) -> list[Movie]:
    stmt = select(Movie).order_by(Movie.id.desc())
    return list(db.execute(stmt).scalars().all())


def create_movie(db: Session, movie: Movie) -> Movie:
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie
