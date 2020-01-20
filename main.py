import inspect
from typing import List

import typing

from Common.JsonLogic.JsonContract import JsonContract
from Common.JsonLogic.JsonFormatter import JsonFormatter
from Common.NetworkLogic.Request.RequestDto import RequestDto
from Entities.Student.Student import Student
from Modules.ServerManager import ServerManager


class Temp(JsonContract):
    my_list: List[str]
    dto: RequestDto[Student]

    @property
    def _json_fields(self) -> dict:
        return {
            "d": "dto",
            "m": "my_list"
        }


def main():
    # ServerManager.start_server()
    t = Temp()
    t.my_list = ["qwe", "wer"]
    t.dto = RequestDto("GetStudent", Student.get_test_student())
    t_json = JsonFormatter.serialize(t)
    t_val = JsonFormatter.deserialize(t_json, Temp)
    print()


if __name__ == '__main__':
    main()
