from unittest.mock import Mock, patch

from .factory import EmployeeFactory
from ..models import ManyEmployees
import random


def test_get_employees(enable_db, get_client):
    client = get_client
    db = enable_db
    size = random.randint(5, 10)
    employee_factory = EmployeeFactory(db)
    employee_factory.create_batch(size)
    employees = ManyEmployees(employees=list(db.employee.find()))
    with patch('main.get_db', Mock(return_value=db)):
        res = client.get('/employees')
    assert res.json()['employees'] == employees.dict()['employees']
