from app.models import StudentIn
from tests.utils.utils import random_lower_string, random_tg


def get_student_in() -> StudentIn:
    tg_id = random_tg()
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_lower_string()
    return StudentIn(
        tg_id=tg_id, first_name=first_name, last_name=last_name, username=username
    )
