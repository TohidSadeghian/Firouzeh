import validators
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .schemas import UrlShortenerCreate, UrlShortenerRedirect
from ..dependencies import get_db
from .messages import Messages
from .service import UrlShortenerHandler


router = APIRouter()

@router.post('/create_url/', response_model=UrlShortenerRedirect, status_code=status.HTTP_201_CREATED)
async def create_shortened_url(url:UrlShortenerCreate, db: Session = Depends(get_db)):
    """
    Api for creating shortened url
    request body: contains a valid link(original_url)
    response body: orginal_url & shortened_url
    """
    if not validators.url(url.original_url):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=Messages.URL_NOT_VALID.value)
    
    obj = await UrlShortenerHandler().create_short_url(db=db, url=url)
    return UrlShortenerRedirect(original_url=obj.original_url, shortened_url=obj.shortened_url)


@router.get("/{url_key}", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def forward_to_target_url(
        url_key: str,
        db: Session = Depends(get_db)
):
    """
    Api for redirecting to original url

    """
    if db_url := await UrlShortenerHandler().get_url_obj(db=db, url_key=url_key):
        return RedirectResponse(db_url)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=Messages.URL_NOT_FOUND.value)
