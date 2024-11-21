import string
import secrets
from ..config import URL_SHORTENER_CHAR_LEN


async def generate_random_key(length: int = URL_SHORTENER_CHAR_LEN) -> str:
    """
    this function will create a string with len 'URL_SHORTENER_CHAR_LEN' and
    containing 26 + 10 digit
    total unique keys will be 36^5
    """
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))



