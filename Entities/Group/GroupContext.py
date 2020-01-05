from Common.Entity.BaseEntityContext import BaseEntityContext
from Common.JsonFormatter.JsonFormatter import JsonFormatter
from Entities.Group.Group import Group


class GroupContext(BaseEntityContext[Group]):

    def __init__(self, entity_json: str = None) -> None:
        if entity_json is not None:
            student = JsonFormatter.deserialize(entity_json, Group)
            super().__init__(student)
