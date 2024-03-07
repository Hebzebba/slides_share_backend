from ..model.create_model import CreateAdmin
from ..model.update_model import UpdateAdmin
from ..model.model import Admin
from sqlmodel import select, Session
from fastapi import HTTPException
from ..utils import hash_password


def add_admin_service(admin: CreateAdmin, db_session: Session) -> dict:
    try:
        db_session.add(
            Admin(
                name=admin.name,
                role="Admin",
                password=hash_password(admin.password)
            )
        )
        db_session.commit()
        return {"message": "admin created successful"}
    except Exception :
        raise HTTPException(status_code=400, detail="admin already exist")


def delete_admin_service(admin_id: str, db_session: Session) -> dict:
    result_set = db_session.get(Admin, admin_id)
    if not result_set:
        raise HTTPException(status_code=400, detail="Admin does not exit")
    db_session.delete(result_set)
    db_session.commit()
    return {"message": "admin deleted"}


def update_admin_service(admin: UpdateAdmin, db_session: Session) -> dict:
    result_set = db_session.get(Admin, admin.id)
    if not result_set:
        raise HTTPException(status_code=400, detail="admin not found")

    result_set.name = admin.name
    result_set.role = admin.role
    result_set.password = admin.password
    db_session.add(result_set)
    db_session.commit()
    return {"message": "admin updated"}


def get_admin_by_id_number_service(admin_id: str, db_session: Session) -> dict:
    result_set = db_session.get(Admin, admin_id)
    if result_set:
        return result_set
    raise HTTPException(status_code=400, detail="admin not found")

def get_admin_by_name_service(name: str, db_session: Session) -> dict:
    try:
        statement = select(Admin).where(Admin.name == name)
        result_set = db_session.exec(statement).one()
        if result_set:
            return result_set
    except Exception:
        raise HTTPException(status_code=400, detail="admin not found")


def get_all_admins_service(db_session: Session) -> list[dict]:
    statement = select(Admin)
    result = db_session.exec(statement)
    return result.all()
