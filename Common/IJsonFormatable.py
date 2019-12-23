from abc import ABCMeta, abstractmethod


class IJsonFormatable:
    """Each class that will override this class must have annotations for all fields."""

    __metaclass__ = ABCMeta
    __json_to_field: dict = NotImplemented

    @abstractmethod
    def to_json(self) -> dict:
        """format object to json"""

    def json_to_field(self, min_field: str) -> str:
        """convert minimize field to full name field"""
        return self.__json_to_field[min_field]
