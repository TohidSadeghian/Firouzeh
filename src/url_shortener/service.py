from sqlalchemy.orm import Session
from .models import URLShortener as UrlShortnerModel
from .schemas import UrlShortenerCreate
from .utils import generate_random_key


class UrlShortenerHandler:
    
    def create_short_url(self, db: Session, url: UrlShortenerCreate):
        shortened_url = self.get_unique_string(db)
        obj = UrlShortnerModel(
            shortened_url=shortened_url, original_url=url.original_url
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get_db_url_by_key(self, db: Session, url_key: str) -> UrlShortnerModel:
        return (
            db.query(UrlShortnerModel)
            .filter(UrlShortnerModel.shortened_url == url_key)
            .first()
        )

    def get_unique_string(self, db: Session)-> str:
        key = generate_random_key()
        while self.get_db_url_by_key(db, key):
            key = generate_random_key()
        return key
