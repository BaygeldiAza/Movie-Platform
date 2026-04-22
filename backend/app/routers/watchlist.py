from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.watchlist import WatchlistCreate, WatchlistResponse
from app.services.watchlist_service import get_user_watchlist, add_movie_to_watchlist, remove_from_watchlist
from app.core.dependencies import get_db, get_current_user
from app.models.user import User

router = APIRouter()

@router.get("", response_model=List[WatchlistResponse])
async def get_my_watchlist(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await get_user_watchlist(db, current_user.id)

@router.post("", response_model=WatchlistResponse)
async def add_to_watchlist(
    watchlist_in: WatchlistCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await add_movie_to_watchlist(db, watchlist_in, current_user.id)

@router.delete("/{watchlist_id}")
async def remove_from_watchlist(
    watchlist_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    await remove_from_watchlist(db, watchlist_id, current_user.id)
    return {"message": "Removed from watchlist"}