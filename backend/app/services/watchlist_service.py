from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.watchlist import Watchlist
from app.schemas.watchlist import WatchlistCreate
from app.core.exceptions import BadRequestException, NotFoundException

async def get_user_watchlist(db: AsyncSession, user_id: int):
    result = await db.execute(select(Watchlist).where(Watchlist.user_id == user_id))
    return result.scalars().all()

async def add_movie_to_watchlist(db: AsyncSession, watchlist_in: WatchlistCreate, user_id: int):
    exists = await db.execute(
        select(Watchlist).where(
            Watchlist.user_id == user_id,
            Watchlist.movie_id == watchlist_in.movie_id
        )
    )
    if exists.scalar_one_or_none():
        raise BadRequestException("Movie already in watchlist")

    db_item = Watchlist(user_id=user_id, movie_id=watchlist_in.movie_id)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

async def remove_from_watchlist(db: AsyncSession, watchlist_id: int, user_id: int):
    item = await db.execute(
        select(Watchlist).where(
            Watchlist.id == watchlist_id,
            Watchlist.user_id == user_id
        )
    )
    item = item.scalar_one_or_none()
    if not item:
        raise NotFoundException("Watchlist item not found")

    await db.delete(item)
    await db.commit()
    return True