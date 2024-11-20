import string
import secrets
from sqlalchemy.orm import Session


def generate_random_key(length: int = 5) -> str:
    """
    this function will create a string with len 5 and
    containing 26 + 10 digit
    total unique keys will be 36^5
    """
    chars = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))



