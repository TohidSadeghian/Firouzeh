from .url_shortener.database import SessionLocal
from .config import REDIS_PASSWORD, REDIS_NAMESPACE
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


from aiocache import Cache


def redis_cache():
    return Cache.REDIS(endpoint="urlshortener_redis", port=6379, password=REDIS_PASSWORD,namespace=REDIS_NAMESPACE)

cache = redis_cache()