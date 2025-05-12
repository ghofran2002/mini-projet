from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    department_id: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: str
