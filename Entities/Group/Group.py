from Common.Entity.BaseEntity import BaseEntity
from Entities.EntityType import EntityType
from Entities.Group.GroupData import GroupData


class Group(BaseEntity[GroupData]):
    entity_type: EntityType = EntityType.group

    def __init__(self, id_entity: int = None, data: GroupData = None) -> None:
        super().__init__(id_entity, data)

    @staticmethod
    def get_test_group():
        group_data = GroupData.get_test_group_data()
        group = Group(group_data.Id, group_data)
        return group
