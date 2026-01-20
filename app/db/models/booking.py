from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), primary_key=True, autoincrement=True
    )

    showtime_id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True),
        ForeignKey("showtimes.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    customer_name: Mapped[str] = mapped_column(String(120), nullable=False)
    customer_phone: Mapped[str | None] = mapped_column(String(30), nullable=True)

    seats: Mapped[int] = mapped_column(SMALLINT(unsigned=True), nullable=False)

    status: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="confirmed"
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

    showtime = relationship("Showtime", back_populates="bookings")
