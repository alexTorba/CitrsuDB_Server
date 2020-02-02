from typing import List

from Common.JsonLogic.JsonContract import JsonContract
from Common.JsonLogic.JsonTest.TestEntities.Univercity.University import University


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
    def get_test_city():
        c = City()
        c.name = "Kharkov"
        c.universities = [University.get_test_university(), University.get_test_university(),
                          University.get_test_university()]
        return c
