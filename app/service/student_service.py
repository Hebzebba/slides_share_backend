from ..model.create_model import CreateStudent
from ..model.model import Student
from sqlmodel import select, Session
from fastapi import HTTPException
from ..utils import hash_password


def add_student_service(student: CreateStudent, db_session: Session) -> dict:
    try:
        db_session.add(
            Student(
                name=student.username,
                password=hash_password(student.password),
                index_number=student.index_number
            )
        )
        db_session.commit()
        return {"message": "student created successful"}
    except Exception :
        raise HTTPException(status_code=400, detail="student already exist")


def delete_student_service(index_number: str, db_session: Session) -> dict:
    result_set = db_session.get(Student, index_number)
    if not result_set:
        raise HTTPException(status_code=400, detail="Student does not exit")
    db_session.delete(result_set)
    db_session.commit()
    return {"message": "student deleted"}


def update_student_service(student: CreateStudent, db_session: Session) -> dict:
    result_set = db_session.get(Student, student.index_number)
    if not result_set:
        raise HTTPException(status_code=400, detail="student not found")

    result_set.studentname = student.studentname
    result_set.password = student.password
    db_session.add(result_set)
    db_session.commit()
    return {"message": "student updated"}


def get_student_by_index_number_service(index_number: str, db_session: Session) -> dict:
    result_set = db_session.get(Student, index_number)
    if result_set:
        return result_set
    raise HTTPException(status_code=400, detail="student not found")


def get_all_students_service(db_session: Session) -> list[dict]:
    statement = select(Student)
    result = db_session.exec(statement)
    return result.all()