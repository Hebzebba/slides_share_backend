from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..dep.shared_dependencies import DB_SESSION
from ..service.student_service import get_student_by_index_number_service
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

    return {"status":"success", "username":result.name}