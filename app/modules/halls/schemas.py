from pydantic import BaseModel, Field


class HallCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    capacity: int = Field(..., gt=0, lt=5000)


class HallOut(BaseModel):
    id: int
    name: str
    capacity: int
