from Common.Entity.BaseEntity import BaseEntity
from Common.JsonLogic.JsonFormatter import JsonFormatter
from Entities.EntityType import EntityType
from Entities.Group.Group import Group
from Entities.Student.Student import Student


class EntityFactory:
    @staticmethod
    def create_entity(entity_type: EntityType, entity_json: str) -> BaseEntity:
        if entity_type is EntityType.student:
            return JsonFormatter.deserialize(entity_json, Student)
        elif entity_type is EntityType.group:
            return JsonFormatter.deserialize(entity_json, Group)
