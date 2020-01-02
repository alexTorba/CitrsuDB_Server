from Common.Entity.IEntity import IEntity
from Common.JsonFormatter.JsonContract import JsonContract
from Entities.EntityType import EntityType


class Student(IEntity):
    Id: int
    data: JsonContract
    entity_type: EntityType

    def __init__(self, entity_id: int, data: JsonContract) -> None:
        self.Id = entity_id
        self.data = data
        self.entity_type = EntityType.student
