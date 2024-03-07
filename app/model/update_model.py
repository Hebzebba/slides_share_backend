from sqlmodel import SQLModel

class UpdateStudent(SQLModel):
    index_number: str
    username: str
    role: str
    password: str


class UpdateLecturer(SQLModel):
    email: str
    name: str
    role: str
    password: str

class UpdateAdmin(SQLModel):
    id: int
    name: str
    role: str
    password: str
