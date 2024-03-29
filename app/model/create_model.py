from sqlmodel import SQLModel

class CreateStudent(SQLModel):
    index_number: str
    username: str
    password: str


class CreateLecturer(SQLModel):
    email: str
    name: str
    password: str

class CreateAdmin(SQLModel):
    name: str
    password: str
