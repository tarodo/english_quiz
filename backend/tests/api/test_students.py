from app.api.students import StudentErrors
from app.crud import students
from fastapi.testclient import TestClient
from sqlmodel import Session
from tests.utils.students import get_student_in
from tests.utils.users import create_random_user


def test_create_student_by_admin(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    user = create_random_user(db)
    student_in = get_student_in(user.id)
    data = student_in.dict()
    r = client.post(f"/students/", headers=superuser_token_headers, json=data)
    assert 200 <= r.status_code < 300
    created_student = r.json()
    student = students.read_by_tg_id(db, tg_id=student_in.tg_id)
    assert student
    assert student.tg_id == created_student["tg_id"]


def test_create_student_by_user_by_itself(
    client: TestClient, user_token_headers: dict[str, str], db: Session
) -> None:
    user = create_random_user(db)
    student_in = get_student_in(user.id)
    data = student_in.dict()
    r = client.post(f"/students/", headers=user_token_headers, json=data)
    assert r.status_code == 400
    created_student = r.json()
    assert created_student["detail"]["err"] == str(StudentErrors.NoRightsForUser)


def test_create_student_same(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    user = create_random_user(db)
    student_in = get_student_in(user.id)
    student = students.create(db, payload=student_in)
    data = student_in.dict()
    r = client.post(f"/students/", headers=superuser_token_headers, json=data)
    assert r.status_code == 400
    created_student = r.json()
    assert created_student["detail"]["err"] == str(StudentErrors.StudentExists)
