from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER


SQLALCHEMY_DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@urshortener_db/{DATABASE_NAME}'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()