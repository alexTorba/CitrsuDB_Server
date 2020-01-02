from Common.Entity.IEntity import IEntity
from Common.JsonFormatter.JsonContract import JsonContract
from Entities.EntityType import EntityType


class Group(IEntity):
    Id: int
    data: JsonContract
    entity_type: EntityType

    def __init__(self, id_entity: int, data: JsonContract) -> None:
        self.Id = id_entity
        self.data = data
        self.entity_type = EntityType.group
