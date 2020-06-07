from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class Employee(BaseModel):
    id: ObjectIdStr = Field(alias="_id")
    name: str
    email: str
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int


class ManyEmployees(BaseModel):
    employees: List[Employee]
