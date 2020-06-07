from typing import List

from faker import Faker

from ..models import Employee

fake = Faker()


class EmployeeFactory:
    model = Employee

    def __init__(self, db):
        self.employee_collection = db.employee

    def make_instance(self) -> dict:
        data = {
            'name': fake.name(),
            'email': fake.email(),
            'age': fake.pyint(min_value=18, max_value=65),
            'company': fake.company(),
            'join_date': fake.past_datetime().isoformat(),
            'job_title': fake.job(),
            'gender': fake.random_element(['male', 'female']),
            'salary': fake.pyint(min_value=1000, max_value=9999)
        }
        assert (set(data.keys()) ==
                set([key for key in self.model.__dict__['__fields__'].keys()
                    if key not in ('id', '_id')]))
        return data

    def create(self) -> dict:
        instance = self.make_instance()
        self.employee_collection.insert_one(instance)
        return instance

    def create_batch(self, size: int) -> List[dict]:
        instances = list()
        for _ in range(size):
            instance = self.make_instance()
            instances.append(instance)
        self.employee_collection.insert_many(instances)
        return instances
