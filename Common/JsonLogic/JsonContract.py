import types
from abc import ABC, abstractmethod
from copy import copy
from typing import Dict

from Entities.EntityType import EntityType


class JsonContract(ABC):
    """Each class that will override this class must have :\n
    - annotations for all fields\n
    - implement _json_field\n
    - open ctor\n"""

    @property
    @abstractmethod
    def _json_fields(self) -> dict:  # key = minimized field name, value = full field name
        pass

    # key = full field name, value = minimized field name
    __field_json: dict = NotImplemented

    def to_minimize_dict(self) -> dict:
        """format object to minimize dict"""
        if self.__field_json is NotImplemented:
            self.__field_json = dict(zip(self._json_fields.values(), self._json_fields.keys()))
        return {self.__field_json[n]: copy(v) for n, v in self.__get_full_dict().items()
                if JsonContract.__filter_items(n, v)}

    @staticmethod
    def __filter_items(n: str, v):
        if n.startswith("_") \
                or isinstance(v, types.FunctionType) \
                or isinstance(v, staticmethod) \
                or isinstance(v, classmethod) \
                or isinstance(v, property) \
                or isinstance(v, EntityType):
            return False
        return True

    def __get_full_dict(self) -> dict:
        return dict(self.__dict__, **self.__class__.__dict__)

    def _update_json_fields(self, json_fields: Dict[str, str]) -> None:
        self._json_fields.update(json_fields)

    def json_to_field(self, min_field: str) -> str:
        """convert minimize field to full name field"""
        return self._json_fields.get(min_field)
