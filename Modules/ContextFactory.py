from Entities.EntityType import EntityType
from Entities.Group.GroupContext import GroupContext
from Entities.Student.StudentContext import StudentContext


class ContextFactory:

    @staticmethod
    def create_context(entity_type: EntityType, json: str):
        if entity_type is EntityType.student:
            return StudentContext(json)
        elif entity_type is EntityType.group:
            return GroupContext(json)
