from pydantic import BaseModel


class UrlShortenerCreate(BaseModel):
	original_url: str


class UrlShortenerRedirect(UrlShortenerCreate):
	shortened_url: str