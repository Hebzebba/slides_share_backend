from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from ..dep.shared_dependencies import DB_SESSION
from ..service.student_service import get_student_by_index_number_service
from ..service.lecturer_service import get_lecturer_by_email_service
from ..service.admin_service import get_admin_by_name_service
from ..utils import verify_hash_password


auth_controller = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30


@auth_controller.post("/login", tags=["Auth"])
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db_session: DB_SESSION
):
    index_number = form_data.username
    result = get_student_by_index_number_service(index_number, db_session)
    if not verify_hash_password(form_data.password, result.password):
        raise HTTPException(status_code=400, detail="Invalid pasword")

    content = {"status":"success", "username":result.name, "role": result.role, "index_number": result.index_number}
    return JSONResponse(content)


@auth_controller.post("/login/lecturer", tags=["Auth"])
def lecturer_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db_session: DB_SESSION
):
    email = form_data.username
    result = get_lecturer_by_email_service(email, db_session)
    if not verify_hash_password(form_data.password, result.password):
        raise HTTPException(status_code=400, detail="Invalid pasword")

    content = {"status":"success", "username":result.name, "role": result.role, "email":result.email}
    return JSONResponse(content)


@auth_controller.post("/login/admin", tags=["Auth"])
def lecturer_login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db_session: DB_SESSION
):
    name = form_data.username
    result = get_admin_by_name_service(name, db_session)
    if not verify_hash_password(form_data.password, result.password):
        raise HTTPException(status_code=400, detail="Invalid pasword")

    content = {"status":"success", "username":result.name, "role": result.role}
    return JSONResponse(content)