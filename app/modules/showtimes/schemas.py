from datetime import datetime

from pydantic import BaseModel, Field


class ShowtimeCreate(BaseModel):
    movie_id: int = Field(..., gt=0, description="ID of the movie")
    hall_id: int = Field(..., gt=0, description="ID of the hall")
    starts_at: datetime
    price: float = Field(..., ge=0, description="Price of the showtime")
    status: str = Field(
        default="scheduled", max_length=20, description="Status of the showtime"
    )


class ShowtimeOut(BaseModel):
    id: int
    movie_id: int
    hall_id: int
    starts_at: datetime
    price: float
    status: str
