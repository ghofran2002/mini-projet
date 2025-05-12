from fastapi import APIRouter
from app.database.mongo import db
from app.models.student import StudentCreate, StudentOut
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=StudentOut)
async def create_student(student: StudentCreate):
    student_dict = student.dict()
    student_dict["courses"] = []
    result = await db["students"].insert_one(student_dict)
    return StudentOut(id=str(result.inserted_id), **student_dict)

@router.get("/", response_model=list[StudentOut])
async def list_students():
    students = []
    async for doc in db["students"].find():
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        students.append(StudentOut(**doc))
    return students

@router.post("/{student_id}/enroll/{course_id}")
async def enroll_student(student_id: str, course_id: str):
    await db["students"].update_one({"_id": ObjectId(student_id)}, {"$addToSet": {"courses": course_id}})
    return {"msg": "Student enrolled successfully"}
