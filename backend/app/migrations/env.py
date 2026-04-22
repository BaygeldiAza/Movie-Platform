from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from app.db.database import Base
from app.models.user import User
from app.models.movie import Movie
from app.models.watchlist import Watchlist
from app.core.config import settings

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    url = settings.DATABASE_URL
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    conf = config.get_section(config.config_ini_section)
    conf["sqlalchemy.url"] = settings.DATABASE_URL
    connectable = engine_from_config(conf, prefix="sqlalchemy.", poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()