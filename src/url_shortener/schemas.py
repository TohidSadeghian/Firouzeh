from pydantic import BaseModel


class UrlShortenerCreate(BaseModel):
	original_url: str


class UrlShortenerRedirect(BaseModel):
	shortened_url: str