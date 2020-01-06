from Common.JsonLogic.JsonContract import JsonContract
from typing import TypeVar
T = TypeVar("T", bound=JsonContract)


class BaseRequestDto(JsonContract):
    server_method: str

    _json_fields = {
        "s": "server_method",
    }
