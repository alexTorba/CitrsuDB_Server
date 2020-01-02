from Common.Entity.IEntity import IEntity
from Common.JsonFormatter.JsonContract import JsonContract
from Entities.EntityType import EntityType
from Entities.Group.GroupData import GroupData


class Group(JsonContract, IEntity):
    Id: int
    data: JsonContract
    entity_type = EntityType.group

    _json_fields = {
        "i": "Id",
        "d": "data"
    }

    def __init__(self, id_entity: int, data: JsonContract) -> None:
        self.Id = id_entity
        self.data = data
    
    
    @staticmethod
    def get_test_group():
        group_data = GroupData.get_test_group_data()
        group = Group(group_data.Id, group_data)
        return group

    