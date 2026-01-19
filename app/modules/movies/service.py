from sqlalchemy.orm import Session

from app.db.models.movie import Movie
from app.modules.movies.repo import create_movie, list_movies
from app.modules.movies.schemas import MovieCreate, MovieOut


def get_movies(db: Session) -> list[MovieOut]:
    movies = list_movies(db)
    return [
        MovieOut(
            id=m.id,
            title=m.title,
            duration_minutes=m.duration_minutes,
            rating=m.rating,
            created_at=m.created_at,
        )
        for m in movies
    ]


def add_movie(db: Session, payload: MovieCreate) -> MovieOut:
    new_movie = Movie(
        title=payload.title,
        duration_minutes=payload.duration_minutes,
        rating=payload.rating,
    )
    created_movie = create_movie(db, new_movie)
    return MovieOut(
        id=created_movie.id,
        title=created_movie.title,
        duration_minutes=created_movie.duration_minutes,
        rating=created_movie.rating,
    )
