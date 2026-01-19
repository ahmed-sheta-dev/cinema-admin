from flask import g
from sqlalchemy.orm import Session

from app.extensions import SessionLocal


def get_db() -> Session:
    if "db" not in g:
        g.db = SessionLocal()
    return g.db


def close_db(e=None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()
