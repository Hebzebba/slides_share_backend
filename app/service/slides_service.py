from ..model.model import Slides
from sqlmodel import select, Session
from fastapi import HTTPException
import shutil, os


def add_slides_service(
    db_session: Session, host_url, course, department, level, semister, slides, lecturer_id
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
                semister=semister,
                content_type=slides.content_type,
                file_upload=f"{host_url}/slides/{slides.filename}",
                lecturer_id=lecturer_id
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

# TODO
# def update_slides_service(db_session: Session, host_url, _id, course, department, level, semister, slides, lecturer_id) -> dict:
#     result_set = db_session.get(Slides, _id)
#     if not result_set:
#         raise HTTPException(status_code=400, detail="Slides not found")

#     result_set.course = course
#     result_set.department = department
#     result_set.level = level
#     result_set.semister = semister
#     result_set.lecturer_id = lecturer_id
#     db_session.add(result_set)
#     db_session.commit()
#     return {"message": "lecturer updated"}



def get_all_slides_service(db_session: Session) -> list[dict]:
    statement = select(Slides)
    result = db_session.exec(statement)
    return result.all()
