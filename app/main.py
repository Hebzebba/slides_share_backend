from fastapi import FastAPI
from .controller.student_controller import student_controller
from .controller.lecturer_controller import lecturer_controller
from .controller.admin_controller import admin_controller
from .controller.slides_controller import slides_controller
from .controller.auth_controller import auth_controller
from .model.model import create_db, drop_db
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.on_event("startup")
def on_startup():
    # drop_db()  # enable this in dev mode
    create_db()


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
