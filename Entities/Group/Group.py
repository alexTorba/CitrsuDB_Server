from typing import List

from Common.JsonContract import JsonContract
from Entities.Student.Student import Student


class Group(JsonContract):
    Id: int
    Name: str
    Photo: bytearray
    Students: List[Student]

    _json_field = {
        "i": "Id",
        "n": "Name",
        "p": "Photo",
        "s": "Students"
    }

    @staticmethod
    def get_test_group():
        group = Group()
        group.Id = 1
        group.Name = "КИУКИ 16-4"
        group.Students = [Student.get_test_student()]
        return group
