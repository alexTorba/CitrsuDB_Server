from typing import List

from Common.JsonLogic.JsonContract import JsonContract
from Entities.Group.GroupData import GroupData


class UniversityData(JsonContract):
    name: str
    groups: List[GroupData]
    some_list: List[int]

    @property
    def _json_fields(self) -> dict:
        return {
            "n": "name",
            "g": "groups",
            "s": "some_list"
        }
