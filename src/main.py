from fastapi import FastAPI
from src.url_shortener.router import router as UrlShortner_router

app = FastAPI()
app.include_router(UrlShortner_router, tags=['url shortener'])