from fastapi import APIRouter
from ..dep.shared_dependencies import DB_SESSION
from ..config import BASE_ROUTER
from ..model.create_model import CreateAdmin
from ..model.update_model import UpdateAdmin
from ..service.admin_service import add_admin_service, delete_admin_service, update_admin_service, get_all_admins_service, get_admin_by_id_number_service


admin_controller = APIRouter()


@admin_controller.post(f"{BASE_ROUTER}/admin/register", tags=["admin"])
def register_admin(admin: CreateAdmin, db_session: DB_SESSION) -> dict:
    return add_admin_service(admin, db_session)


@admin_controller.delete(f"{BASE_ROUTER}/admin/delete", tags=["admin"])
def delete_admin( admin_id: str, db_session: DB_SESSION) -> dict:
    return delete_admin_service(admin_id, db_session)


@admin_controller.put(f"{BASE_ROUTER}/admin/update", tags=["admin"])
def update_admin( admin: UpdateAdmin, db_session: DB_SESSION) -> dict:
    return update_admin_service(admin, db_session)


@admin_controller.get(f"{BASE_ROUTER}/admin/all", tags=["admin"])
def all_admins( db_session: DB_SESSION):
    return get_all_admins_service(db_session)


@admin_controller.get(f"{BASE_ROUTER}/admin", tags=["admin"])
def single_admin( admin_id: str, db_session: DB_SESSION):
    return get_admin_by_id_number_service(admin_id, db_session)
