from pydantic import BaseModel, Field


class MovieCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    duration_minutes: int = Field(..., gt=1, lt=600)
    rating: str | None = Field(None, max_length=10)


class MovieOut(BaseModel):
    id: int
    title: str
    duration_minutes: int
    rating: str | None
