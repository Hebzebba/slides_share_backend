from fastapi import APIRouter
from ..dep.shared_dependencies import DB_SESSION
from ..config import BASE_ROUTER
from ..model.create_model import CreateLecturer
from ..service.lecturer_service import add_lecturer_service, delete_lecturer_service, update_lecturer_service, get_all_lecturers_service, get_lecturer_by_id_number_service


lecturer_controller = APIRouter()


@lecturer_controller.post(f"{BASE_ROUTER}/lecturer/register", tags=["lecturer"])
def register_lecturer(lecturer: CreateLecturer, db_session: DB_SESSION) -> dict:
    return add_lecturer_service(lecturer, db_session)


@lecturer_controller.delete(f"{BASE_ROUTER}/lecturer/delete", tags=["lecturer"])
def delete_lecturer( lecturer_id: str, db_session: DB_SESSION) -> dict:
    return delete_lecturer_service(lecturer_id, db_session)


@lecturer_controller.put(f"{BASE_ROUTER}/lecturer/update", tags=["lecturer"])
def update_lecturer( lecturer: CreateLecturer, db_session: DB_SESSION) -> dict:
    return update_lecturer_service(lecturer, db_session)


@lecturer_controller.get(f"{BASE_ROUTER}/lecturer/all", tags=["lecturer"])
def all_lecturers( db_session: DB_SESSION):
    return get_all_lecturers_service(db_session)


@lecturer_controller.get(f"{BASE_ROUTER}/lecturer", tags=["lecturer"])
def single_lecturer( lecturer_id: str, db_session: DB_SESSION):
    return get_lecturer_by_id_number_service(lecturer_id, db_session)
