from fastapi import APIRouter
from ..dep.shared_dependencies import DB_SESSION
from ..config import BASE_ROUTER
from ..model.create_model import CreateStudent
from ..model.update_model import UpdateStudent
from ..service.student_service import add_student_service, delete_student_service, update_student_service, get_all_students_service, get_student_by_index_number_service


student_controller = APIRouter()


@student_controller.post(f"{BASE_ROUTER}/student/register", tags=["student"])
def register_student(student: CreateStudent, db_session: DB_SESSION) -> dict:
    return add_student_service(student, db_session)


@student_controller.delete(f"{BASE_ROUTER}/student/delete", tags=["student"])
def delete_student( index_number: str, db_session: DB_SESSION) -> dict:
    return delete_student_service(index_number, db_session)


@student_controller.put(f"{BASE_ROUTER}/student/update", tags=["student"])
def update_student( student: UpdateStudent, db_session: DB_SESSION) -> dict:
    return update_student_service(student, db_session)


@student_controller.get(f"{BASE_ROUTER}/student/all", tags=["student"])
def all_students( db_session: DB_SESSION):
    return get_all_students_service(db_session)


@student_controller.get(f"{BASE_ROUTER}/student", tags=["student"])
def single_student( index_number: str, db_session: DB_SESSION):
    return get_student_by_index_number_service(index_number, db_session)
