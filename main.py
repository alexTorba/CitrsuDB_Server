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
    e.person.age = 10
    e.person.first_name = "Alex"
    e.person.last_name = "Torba"
    e.person.middle_name = "Olegovich"

    e.citizenship = "Ukraine"
    e.salary = 20000
    e.knowledge_of_language = ["English", "Russian", "Ukraine"]

    json_e = JsonFormatter.dumps(e)
    print(json_e)
    emp = JsonFormatter.loads(json_e, Employee)
    print(emp.__eq__(e))


class Person(IJsonFormatable):
    age: int
    first_name: str
    last_name: str
    middle_name: str

    json_field_view: dict = {
        "a": "age",
        "f": "first_name",
        "l": "last_name",
        "m": "middle_name"
    }

    def to_json(self) -> dict:
        return {
            "a": self.age,
            "f": self.first_name,
            "l": self.last_name,
            "m": self.middle_name
        }


class Employee(IJsonFormatable):
    person: Person
    salary: int
    citizenship: str
    knowledge_of_language: List[str]

    json_field_view: dict = {
        "p": "person",
        "s": "salary",
        "c": "citizenship",
        "k": "knowledge_of_language"
    }

    def to_json(self) -> dict:
        return {
            "p": self.person,
            "s": self.salary,
            "c": self.citizenship,
            "k": self.knowledge_of_language
        }

    def temp(self) -> str:
        return self.person.__str__()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Employee) and isinstance(o.person, Person):
            return True

        return super().__eq__(o)


class Persons:
    persons: List[Person]

    def __init__(self) -> None:
        p1 = Person()
        p1.first_name = "Alex"

        p2 = Person()
        p2.first_name = "Max"
        self.persons = [p1, p2]


def main():
    # test_json()
    ps = Persons()
    t = ps.__annotations__.get("persons")

    print("")

# try initialize db
# start server


if __name__ == '__main__':
    main()
