import uvicorn
from fastapi import FastAPI

from app.api import login, users, students, tags


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(users.router, prefix="/users", tags=["users"])
    application.include_router(students.router, prefix="/students", tags=["students"])
    application.include_router(tags.router, prefix="/tags", tags=["tags"])
    application.include_router(login.router, tags=["login"])
    return application


app = create_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
