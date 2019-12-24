import typing
from pydoc import locate
from typing import List

from Common.IJsonFormatable import IJsonFormatable
from Common.JsonFormatter import JsonFormatter
from Entities.Group.Group import Group
from Entities.Student.Student import Student
import inspect
import json


def test_json():
    e = Employee()
    e.person = Person()
    e.person = 10
    json_e = JsonFormatter.dumps(e)
    print(json_e)
    emp = JsonFormatter.loads(json_e, Employee)
    

class Person(IJsonFormatable):
    age: int
    json_field_view: dict = {"a": "age"}

    def to_json(self) -> dict:
        return {"a": self.age}


class Employee(IJsonFormatable):
    person: Person
    json_field_view: dict = {"p": "person"}

    def to_json(self) -> dict:
        return {"p": self.person}

    def temp(self) -> str:
        return self.person.__str__()


def main():
    test_json()

# try initialize db
# start server


if __name__ == '__main__':
    main()
