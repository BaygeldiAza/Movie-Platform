from pydantic import BaseModel

class WatchlistCreate(BaseModel):
    movie_id: int

class WatchlistResponse(BaseModel):
    id: int
    user_id: int
    movie_id: int

    class Config:
        from_attributes = True