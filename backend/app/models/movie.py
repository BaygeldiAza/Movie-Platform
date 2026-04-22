from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.db.mixins import TimeStampMixin

class Movie(Base, TimeStampMixin):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
    director = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    rating = Column(Float, default=0.0)
    poster_url = Column(String(500), nullable=True)
    video_url = Column(String(500), nullable=False)  # For free movie streaming

    watchlists = relationship("Watchlist", back_populates="movie")