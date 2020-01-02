from typing import List

from Common.JsonFormatter.JsonContract import JsonContract
from Entities.Student.StudentData import StudentData


class GroupData(JsonContract):
    Id: int
    Name: str
    Photo: bytearray
    Students: List[StudentData]

    @property
    def _json_fields(self) -> dict:
        return {
            "i": "Id",
            "n": "Name",
            "p": "Photo",
            "s": "Students"
        }

    @staticmethod
    def get_test_group_data():
        group_data = GroupData()
        group_data.Id = 1
        group_data.Name = "КИУКИ 16-4"
        group_data.Students = [StudentData.get_test_student()]
        return group_data
