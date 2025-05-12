from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import student, course, department

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(course.router, prefix="/courses", tags=["Courses"])
app.include_router(department.router, prefix="/departments", tags=["Departments"])
