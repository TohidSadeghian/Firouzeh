from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME


SQLALCHEMY_DATABASE_URL = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@urshortener_db/{DATABASE_NAME}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()