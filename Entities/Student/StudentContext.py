from Common.Entity.BaseEntityContext import BaseEntityContext
from Common.JsonFormatter.JsonFormatter import JsonFormatter
from Entities.Student.Student import Student


class StudentContext(BaseEntityContext[Student]):

    def __init__(self, entity_json: str = None) -> None:
        if entity_json is not None:
            student = JsonFormatter.deserialize(entity_json, Student)
            super().__init__(student)
