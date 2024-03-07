from typing import Optional
from sqlmodel import Field, SQLModel
from ..dep.shared_dependencies import engine


class Student(SQLModel, table=True):
    index_number: Optional[str] = Field(default=None, primary_key=True)
    name: str
    role: str
    password: str


class Lecturer(SQLModel, table=True):
    email: Optional[str] = Field(default=None, primary_key=True)
    name: str
    role: str
    password: str


class Admin(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    role: str
    password: str


class Slides(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    course:str
    department:str
    level:str
    semester: str
    file_upload: str
    lecturer_email : Optional[str] = Field(default=None, foreign_key="lecturer.email")


def drop_db():
    SQLModel.metadata.drop_all(bind=engine)


def create_db():
    SQLModel.metadata.create_all(bind=engine)
