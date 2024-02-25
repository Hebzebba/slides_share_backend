# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, ExpiredSignatureError, JWSError, jwt
# from datetime import timedelta, datetime
# from ..config import SECRET_KEY
# from ..database import get_db_session
# from sqlmodel import Session
# from ..service.user_service import get_user_by_email_service

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ALGORITHM = "HS256"


# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# def validate_token_on_request(token: str):
#     db_session: Session = get_db_session()
#     try:
#         decoded = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
#         result = get_user_by_email_service(decoded.get("sub"), db_session)
#         if not result:
#             return False
#     except (JWTError, ExpiredSignatureError, jwt.JWTClaimsError, JWSError):
#         return False
#     return True
