from fastapi import FastAPI
from .controller.student_controller import student_controller
from .controller.lecturer_controller import lecturer_controller
from .controller.admin_controller import admin_controller
from .controller.slides_controller import slides_controller
from .controller.auth_controller import auth_controller
from .service.admin_service import add_admin_service
from .model.model import create_db, drop_db
from .dep.shared_dependencies import get_db_session
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.on_event("startup")
def on_startup():
    # drop_db()  # enable this in dev mode
    create_db()

    # set default username and password for admin
    db_session = get_db_session()
    add_admin_service(db_session)


app.mount("/slides", StaticFiles(directory="slides"), "files")

origins = [
    "http://localhost:3000",
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(student_controller)
app.include_router(lecturer_controller)
app.include_router(admin_controller)
app.include_router(slides_controller)
app.include_router(auth_controller)


@app.get("/")
async def root():
    return {"message": "Hello World"}
