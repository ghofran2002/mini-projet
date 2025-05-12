from fastapi import APIRouter
from app.database.mongo import db
from app.models.department import DepartmentCreate, DepartmentOut
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=DepartmentOut)
async def create_department(dep: DepartmentCreate):
    dep_dict = dep.dict()
    result = await db["departments"].insert_one(dep_dict)
    return DepartmentOut(id=str(result.inserted_id), **dep_dict)

@router.get("/", response_model=list[DepartmentOut])
async def list_departments():
    departments = []
    async for doc in db["departments"].find():
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        departments.append(DepartmentOut(**doc))
    return departments