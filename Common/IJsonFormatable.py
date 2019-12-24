from abc import ABCMeta, abstractmethod


class IJsonFormatable:
    """Each class that will override this class must have annotations for all fields."""

    __metaclass__ = ABCMeta
    json_field_view: dict = NotImplemented

    @abstractmethod
    def to_json(self) -> dict:
        """format object to json"""

    def json_to_field(self, min_field: str) -> str:
        """convert minimize field to full name field"""
        temp_type = type(self.json_field_view)
        return self.json_field_view[min_field]
