import random
import string

from app.models import StudentIn


def random_lower_string(str_len: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=str_len))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string(8)}.com"


def random_tg() -> str:
    return f"{random.randint(1000, 1000000)}"
