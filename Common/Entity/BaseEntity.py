from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from Common.JsonFormatter.JsonContract import JsonContract

T = TypeVar("T", JsonContract, object)


class BaseEntity(Generic[T], JsonContract, ABC):
    id: int
    data: T

    _json_fields = {
        "i": "id",
        "d": "data"
    }

    @property
    @abstractmethod
    def entity_type(self):
        pass

    def __init__(self, id_entity: int = None, data: T = None) -> None:
        if id_entity is not None:
            self.id = id_entity
        if data is not None:
            self.data = data
