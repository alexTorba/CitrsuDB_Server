from typing import List

from Common.JsonContract import JsonContract
from Common.JsonTest.TestEntities.University import University


class City(JsonContract):
    name: str
    universities: List[University]

    @property
    def _json_fields(self) -> dict:
        return {
            "n": "name",
            "u": "universities"
        }

    @staticmethod
    def get_test():
        c = City()
        c.name = "Kharkov"
        c.universities = [University.get_test(), University.get_test(), University.get_test()]
        return c
