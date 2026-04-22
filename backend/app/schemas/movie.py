from pydantic import BaseModel
from typing import Optional

class MovieCreate(BaseModel):
    title: str
    description: Optional[str] = None
    director: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = 0.0
    poster_url: Optional[str] = None
    video_url: str  # For streaming

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    director: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
    poster_url: Optional[str] = None
    video_url: Optional[str] = None

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True