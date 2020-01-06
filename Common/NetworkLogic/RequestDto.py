from typing import TypeVar
from typing import Generic
from Common.JsonFormatter.JsonContract import JsonContract
from Common.NetworkLogic.BaseRequestDto import BaseRequestDto
T = TypeVar("T", bound=JsonContract)


class RequestDto(BaseRequestDto, typing.Generic[T]):
    data: T

    def __init__(self):
        json_field = {"d": "data"}
        self._update_json_fields(json_field)
