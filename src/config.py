import os
# database

DATABASE_USER=os.environ.get("DATABASE_USER")
DATABASE_PASSWORD=os.environ.get("DATABASE_PASSWORD")
DATABASE_NAME=os.environ.get("DATABASE_NAME")

# redis
REDIS_PASSWORD=os.environ.get("REDIS_PASSWORD")
REDIS_NAMESPACE= os.environ.get("REDIS_PASSWORD", "url_shortener")


# Char length for shortened_url
URL_SHORTENER_CHAR_LEN = 5