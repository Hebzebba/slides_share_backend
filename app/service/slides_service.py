from ..model.model import Slides
from sqlmodel import select, Session
from fastapi import HTTPException
import shutil, os


def add_slides_service(
    db_session: Session,
    host_url,
    course,
    department,
    level,
    semester,
    slides,
    lecturer_email,
) -> dict:
    path = f"./slides/{slides.filename}"
    with open(path, "w+b") as file:
        shutil.copyfileobj(slides.file, file)
    try:
        db_session.add(
            Slides(
                course=course,
                department=department,
                level=level,
                semester=semester,
                content_type=slides.content_type,
                file_upload=f"{host_url}/slides/{slides.filename}",
                lecturer_email=lecturer_email,
            )
        )
        db_session.commit()
        return {"message": "slides created successful"}
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=400, detail="failed to create slides")


def delete_slides_service(_id: int, db_session: Session) -> dict:
    result_set = db_session.get(Slides, _id)
    if not result_set:
        raise HTTPException(status_code=400, detail="Slides does not exit")
    
    file_name = result_set.file_upload.split("/")[-1]
    if file_name in os.listdir("./slides"):
        os.remove(f"./slides/{file_name}")

    db_session.delete(result_set)
    db_session.commit()
    return {"message": "Slides deleted"}

def select_slides_using_lecturers_id_service(lecturer_id: str, db_session: Session):
    print(lecturer_id)
    statement = select(Slides).where(Slides.lecturer_email == lecturer_id)
    results = db_session.exec(statement)

    return results.all()

def get_all_slides_service(db_session: Session) -> list[dict]:
    statement = select(Slides)
    result = db_session.exec(statement)
    return result.all()
