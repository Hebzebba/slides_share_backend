from fastapi import APIRouter, File, UploadFile, Form, Request
from typing import Annotated
from ..dep.shared_dependencies import DB_SESSION
from ..config import BASE_ROUTER
from ..service.slides_service import add_slides_service, get_all_slides_service, delete_slides_service, select_slides_using_lecturers_id_service


slides_controller = APIRouter()


@slides_controller.post(f"{BASE_ROUTER}/slides/add", tags=["Slides"])
def add_slides(
    db_session: DB_SESSION,
    request: Request,
    course: Annotated[str, Form()],
    department: Annotated[str, Form()],
    level: Annotated[str, Form()],
    semister: Annotated[str, Form()],
    lecturer_email: Annotated[str, Form()],
    slides: UploadFile = File(...),
) -> dict:
    host_url = f"{request.url.scheme}://{request.url.netloc}"
    
    return add_slides_service(
        db_session, host_url, course, department, level, semister, slides, lecturer_email
    )


@slides_controller.delete(f"{BASE_ROUTER}/slides/delete", tags=["Slides"])
def delete_slides(_id: int, db_session: DB_SESSION) -> dict:
    return delete_slides_service(_id, db_session)


@slides_controller.get(f"{BASE_ROUTER}/slides/lecturer", tags=["Slides"])
def get_slides_using_lecturers_id(lecturer_id: str, db_session: DB_SESSION):
    return select_slides_using_lecturers_id_service(lecturer_id, db_session)


@slides_controller.get(f"{BASE_ROUTER}/slides/all", tags=["Slides"])
def all_slides( db_session: DB_SESSION):
    return get_all_slides_service(db_session)
