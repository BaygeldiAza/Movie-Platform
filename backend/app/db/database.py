from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base

from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL.replace("pymysql", "aiomysql"),
    echo=False,
    pool_pre_ping=True
)
async_session = AsyncSession(engine, expire_on_commit=False)
Base = declarative_base()