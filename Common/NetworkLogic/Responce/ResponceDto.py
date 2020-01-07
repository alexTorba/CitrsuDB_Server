from typing import Generic, TypeVar

from Common.JsonLogic.JsonContract import JsonContract
from Common.NetworkLogic.Responce.BaseResponceDto import BaseResponceDto

T = TypeVar("T", bound=JsonContract)


class ResponceDto(Generic[T], BaseResponceDto):
    data: T

    def __init__(self, status_code: int = None, data: T = None) -> None:
        super().__init__(status_code)
        self.data = data
        json_field = {"d": "data"}
        self._update_json_fields(json_field)
