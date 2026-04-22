from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.movie import MovieCreate, MovieUpdate, MovieResponse
from app.services.movie_service import get_movies, get_movie_by_id, create_movie, update_movie, delete_movie
from app.core.dependencies import get_db

router = APIRouter()

@router.get("", response_model=List[MovieResponse])
async def list_free_movies(skip: int = 0, limit: int = 20, db: AsyncSession = Depends(get_db)):
    return await get_movies(db, skip, limit)

@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie_details(movie_id: int, db: AsyncSession = Depends(get_db)):
    return await get_movie_by_id(db, movie_id)

@router.post("", response_model=MovieResponse)
async def add_movie(movie_in: MovieCreate, db: AsyncSession = Depends(get_db)):
    return await create_movie(db, movie_in)

@router.put("/{movie_id}", response_model=MovieResponse)
async def edit_movie(movie_id: int, movie_in: MovieUpdate, db: AsyncSession = Depends(get_db)):
    return await update_movie(db, movie_id, movie_in)

@router.delete("/{movie_id}")
async def delete_movie(movie_id: int, db: AsyncSession = Depends(get_db)):
    await delete_movie(db, movie_id)
    return {"message": "Movie deleted successfully"}