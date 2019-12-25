from abc import ABCMeta, abstractmethod


class IJsonFormatable:
    """Each class that will override this class must have annotations for all fields."""

    __metaclass__ = ABCMeta
    json_field_view: dict = NotImplemented
    # __view_field_json = json_field_view.__reversed__()

    @abstractmethod
    def to_json(self) -> dict:
        """format object to json"""

    def json_to_field(self, min_field: str) -> str:
        """convert minimize field to full name field"""
        return self.json_field_view[min_field]
