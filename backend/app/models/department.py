from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    name: str

class DepartmentOut(BaseModel):
    id: str
    name: str