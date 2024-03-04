from typing import Annotated
from sqlmodel import Session, create_engine
from fastapi import Depends


connect_args = {"check_same_thread": False}
engine = create_engine("sqlite:///database.db",echo=True, connect_args=connect_args, pool_size=20,max_overflow=0)

def get_db_session() -> Session:
    return Session(bind=engine)

DB_SESSION = Annotated[Session, Depends(get_db_session)]
