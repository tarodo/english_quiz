from app.api import deps
from app.models import StudentIn, StudentOut, User, responses
from fastapi import APIRouter, Depends
from sqlmodel import Session

router = APIRouter()


@router.post("/", response_model=StudentOut, status_code=200, responses=responses)
def create_student(
    payload: StudentIn,
    current_user: User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> User:
    pass
