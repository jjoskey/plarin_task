from urllib.parse import quote_plus

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from pymongo.database import Database

from employees.models import ManyEmployees
from settings import MONGO_PASSWORD, MONGO_URL, MONGO_USER

app = FastAPI()


def get_db() -> Database:
    uri = "mongodb://%s:%s@%s" % (quote_plus(MONGO_USER),
                                  quote_plus(MONGO_PASSWORD), MONGO_URL)
    client = MongoClient(uri)
    return client.local


@app.get('/employees/')
def get_employees_view() -> JSONResponse:
    db = get_db()
    employee_collection = db.employee
    employees = ManyEmployees(employees=list(employee_collection.find()))
    return JSONResponse(status_code=200, content=employees.dict())
