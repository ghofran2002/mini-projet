from pydantic import BaseModel
from typing import List, Optional

class StudentCreate(BaseModel):
    name: str
    email: str
    department_id: str

class StudentOut(BaseModel):
    id: str
    name: str
    email: str
    department_id: str
    courses: Optional[List[str]] = []
