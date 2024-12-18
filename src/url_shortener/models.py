from sqlalchemy import Column, Integer, String, DateTime, func

from .database import Base


class URLShortener(Base):
    """
    model to store original and shortened link
    """
    __tablename__ = "URLShortener"

    id = Column(Integer, primary_key=True)
    original_url = Column(String, index=True)
    shortened_url = Column(String, index=True, unique=True)
    created_at = Column(DateTime, default=func.now())