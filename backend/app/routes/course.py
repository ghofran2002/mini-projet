from fastapi import APIRouter
from app.database.mongo import db
from app.models.course import CourseCreate, CourseOut
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=CourseOut)
async def create_course(course: CourseCreate):
    course_dict = course.dict()
    result = await db["courses"].insert_one(course_dict)
    return CourseOut(id=str(result.inserted_id), **course_dict)

@router.get("/", response_model=list[CourseOut])
async def list_courses():
    courses = []
    async for doc in db["courses"].find():
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        courses.append(CourseOut(**doc))
    return courses