from sqlalchemy.orm import Session
from .models import URLShortener as UrlShortnerModel
from .schemas import UrlShortenerCreate
from .utils import generate_random_key
from ..dependencies import cache


class UrlShortenerHandler:
    async def create_short_url(self, db: Session, url: UrlShortenerCreate):
        shortened_url = await self.get_unique_string(db)
        obj = UrlShortnerModel(
            shortened_url=shortened_url, original_url=url.original_url
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        await cache.set(f"{shortened_url}", f"{url.original_url}")
        return obj

    async def get_url_obj(self, db: Session, url_key: str) -> UrlShortnerModel:
        cached_key = await cache.get(f"{url_key}")
        if cached_key:
            return cached_key
        obj = (
            db.query(UrlShortnerModel)
            .filter(UrlShortnerModel.shortened_url == url_key)
            .first()
        )
        if obj is not None:
            await cache.set(f"{url_key}", f"{obj.original_url}")
            return obj.original_url
        return None

    async def get_unique_string(self, db: Session)-> str:
        key = await generate_random_key()
        while await self.get_url_obj(db, key):
            key = await generate_random_key()
        return key
