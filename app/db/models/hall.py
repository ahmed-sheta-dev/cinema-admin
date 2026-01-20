from sqlalchemy import TIMESTAMP, Integer, SmallInteger, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Hall(Base):
    __tablename__ = "halls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    capacity: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    created_at = mapped_column(
        TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )

    location: Mapped[str | None] = mapped_column(String(120), nullable=True)

    showtimes = relationship("Showtime", back_populates="hall")
