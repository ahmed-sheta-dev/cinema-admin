from pydantic import BaseModel, Field


class BookingCreate(BaseModel):
    showtime_id: int = Field(gt=0)
    customer_name: str = Field(min_length=1, max_length=120)
    customer_phone: str | None = Field(default=None, max_length=30)
    seats: int = Field(ge=1, le=50)


class BookingOut(BaseModel):
    id: int
    showtime_id: int
    customer_name: str
    customer_phone: str | None
    seats: int
    status: str
