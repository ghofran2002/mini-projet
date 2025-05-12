from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str

class CourseOut(BaseModel):
    id: str
    name: str
    description: str