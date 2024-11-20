import validators
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .schemas import UrlShortenerCreate, UrlShortenerRedirect
from ..dependencies import get_db
from .messages import Messages
from .service import UrlShortenerHandler


router = APIRouter()

@router.post('/create_url/', response_model=UrlShortenerRedirect)
def create_shortened_url(url:UrlShortenerCreate, db: Session = Depends(get_db)):
    if not validators.url(url.original_url):
        raise HTTPException(status_code=400, detail=Messages.URL_NOT_VALID.value)
    
    return UrlShortenerHandler().create_short_url(db=db, url=url)
