from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate
from app.core.exceptions import NotFoundException

async def get_movies(db: AsyncSession, skip: int = 0, limit: int = 20):
    result = await db.execute(select(Movie).offset(skip).limit(limit))
    return result.scalars().all()

async def get_movie_by_id(db: AsyncSession, movie_id: int):
    result = await db.execute(select(Movie).where(Movie.id == movie_id))
    movie = result.scalar_one_or_none()
    if not movie:
        raise NotFoundException("Movie not found")
    return movie

async def create_movie(db: AsyncSession, movie_in: MovieCreate):
    db_movie = Movie(**movie_in.model_dump())
    db.add(db_movie)
    await db.commit()
    await db.refresh(db_movie)
    return db_movie

async def update_movie(db: AsyncSession, movie_id: int, movie_in: MovieUpdate):
    movie = await get_movie_by_id(db, movie_id)
    update_data = movie_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(movie, key, value)
    await db.commit()
    await db.refresh(movie)
    return movie

async def delete_movie(db: AsyncSession, movie_id: int):
    movie = await get_movie_by_id(db, movie_id)
    await db.delete(movie)
    await db.commit()
    return True