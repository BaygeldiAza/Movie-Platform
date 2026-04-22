from app.db.database import engine, Base

async def init_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)