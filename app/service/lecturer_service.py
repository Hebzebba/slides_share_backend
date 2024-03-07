from ..model.create_model import CreateLecturer
from ..model.update_model import UpdateLecturer
from ..model.model import Lecturer
from sqlmodel import select, Session
from fastapi import HTTPException
from ..utils import hash_password


def add_lecturer_service(lecturer: CreateLecturer, db_session: Session) -> dict:
    try:
        db_session.add(
            Lecturer(
                name=lecturer.name,
                email=lecturer.email,
                role="Lecturer",
                password=hash_password(lecturer.password)
            )
        )
        db_session.commit()
        return {"message": "lecturer created successful"}
    except Exception :
        raise HTTPException(status_code=400, detail="lecturer already exist")


def delete_lecturer_service(email: str, db_session: Session) -> dict:
    result_set = db_session.get(Lecturer, email)
    if not result_set:
        raise HTTPException(status_code=400, detail="Lecturer does not exit")
    db_session.delete(result_set)
    db_session.commit()
    return {"message": "lecturer deleted"}


def update_lecturer_service(lecturer: UpdateLecturer, db_session: Session) -> dict:
    result_set = db_session.get(Lecturer, lecturer.id)
    if not result_set:
        raise HTTPException(status_code=400, detail="lecturer not found")

    result_set.name = lecturer.name
    result_set.role = lecturer.role
    result_set.password = lecturer.password
    db_session.add(result_set)
    db_session.commit()
    return {"message": "lecturer updated"}


def get_lecturer_by_email_service(email: str, db_session: Session) -> dict:
    result_set = db_session.get(Lecturer, email)
    if result_set:
        return result_set
    raise HTTPException(status_code=400, detail="lecturer not found")


def get_all_lecturers_service(db_session: Session) -> list[dict]:
    statement = select(Lecturer)
    result = db_session.exec(statement)
    return result.all()