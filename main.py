import typing
from pydoc import locate
from typing import List

from Common.IJsonFormatable import IJsonFormatable
from Common.JsonFormatter import JsonFormatter
from Entities.Group.Group import Group
from Entities.Student.Student import Student
import inspect


def test_json():
    e = Employee()
    e.person = Person(10)
    json_e = JsonFormatter.dumps(e)
    print(json_e)
    emp = JsonFormatter.loads(json_e, Employee)


class Person(IJsonFormatable):
    age: int
    __json_to_field: dict = {"a": "age"}

    def to_json(self) -> dict:
        return {"a": self.age}

    def __init__(self, age) -> None:
        self.age = age


class Employee(IJsonFormatable):
    person: Person
    __json_to_field: dict = {"p": "person"}

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
