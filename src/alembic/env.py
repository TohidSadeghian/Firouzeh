from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from logging.config import fileConfig
# ---------------- added code here -------------------------#
import os
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432"

# access to the values within the .ini file in use.
config = context.config# ---------------- added code here -------------------------#
# this will overwrite the ini-file sqlalchemy.url path
# with the path given in the config of the main code
config.set_main_option("sqlalchemy.url", DATABASE_URL)#------------------------------------------------------------## Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata# ---------------- added code here -------------------------#
from url_shortener.models import Base
#------------------------------------------------------------## ---------------- changed code here -------------------------#
# here target_metadata was equal to Nonetarget_metadata = models.Base.metadata
#------------------------------------------------------------#
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:

    from sqlalchemy import create_engine
    import re
    import os

    url_tokens = {
        "DATABASE_USER": os.getenv("DATABASE_USER", ""),
        "DATABASE_PASSWORD": os.getenv("DATABASE_PASSWORD", ""),
        "POSTGRES_HOST": os.getenv("POSTGRES_HOST", ""),
        "DATABASE_NAME": os.getenv("DATABASE_NAME", "")
    }

    url = config.get_main_option("sqlalchemy.url")

    url = re.sub(r"\${(.+?)}", lambda m: url_tokens[m.group(1)], url)

    connectable = create_engine(url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
