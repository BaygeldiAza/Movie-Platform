from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.db.mixins import TimeStampMixin

class Watchlist(Base, TimeStampMixin):
    __tablename__ = "watchlists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)

    user = relationship("User", back_populates="watchlists")
    movie = relationship("Movie", back_populates="watchlists")