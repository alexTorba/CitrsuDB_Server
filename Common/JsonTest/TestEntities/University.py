from typing import List

from Common.JsonContract import JsonContract
from Entities.Group import Group


class University(JsonContract):
    name: str
    groups: List[Group]
    my_list: List

    @property
    def _json_fields(self) -> dict:
        return {
            "n": "name",
            "g": "groups",
            "m": "my_list"
        }

    @staticmethod
    def get_test():
        u = University()
        u.name = "Хнурэ"
        u.groups = [Group.get_test_group(), Group.get_test_group(), Group.get_test_group()]
        u.my_list = [1, 2, 3, 4, 5]
        return u
