from sqlmodel import SQLModel
from typing import Optional

# Student


class CreateStudent(SQLModel):
    index_number: str
    username: str
    password: str


class CreateLecturer(SQLModel):
    name: str
    password: str

# class CreateSlides(SQLModel):
#     course:str
#     department:str
#     level:str
#     semister:str
#     file_upload: str
#     lecturer_id : Optional[int]