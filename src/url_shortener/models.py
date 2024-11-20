from sqlalchemy import Boolean, Column, Integer, String, DateTime, func

from ..database import Base


class URLShortener(Base):
    __tablename__ = "UrlShortener"

    id = Column(Integer, primary_key=True)
    original_url = Column(String, unique=True, index=True)
    shortened_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())