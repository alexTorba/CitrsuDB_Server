from typing import List

from Common.IJsonFormatable import IJsonFormatable
from Entities.Student.Student import Student


class Group(IJsonFormatable):
    Id: int
    Name: str
    Photo: bytearray
    Students: List[Student] = list()

    def to_json(self) -> dict:
        dict_view = {
            "i": self.Id,
            "n": self.Name
        }

        if hasattr(self, "Photo"):
            dict_view["p"] = self.Photo
        if hasattr(self, "Students"):
            dict_view["s"] = self.Students

        return dict_view

    @staticmethod
    def get_test_group():
        group = Group()
        group.Id = 1
        group.Name = "КИУКИ 16-4"
        group.Students = list()
        return group
