from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Showtime(Base):
    __tablename__ = "showtimes"

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), primary_key=True, autoincrement=True
    )
    movie_id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        ForeignKey("movies.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    hall_id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        ForeignKey("halls.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    starts_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, index=True)
    price: Mapped[float] = mapped_column(
        Numeric(10, 2), nullable=False, server_default=text("0.00")
    )
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default=text("'scheduled'")
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP"),
    )

    movie = relationship("Movie", back_populates="showtimes")
    hall = relationship("Hall", back_populates="showtimes")
    bookings = relationship("Booking", back_populates="showtime")
