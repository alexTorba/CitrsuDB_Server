from Common.JsonLogic.JsonContract import JsonContract
from Common.JsonLogic.JsonFormatter import JsonFormatter
from Entities.EntityType import EntityType
from Entities.Group.Group import Group
from Modules.CacheItemManager import CacheItemManager


class GroupManager:
    class GroupDto(JsonContract):
        group: Group

        @property
        def _json_fields(self) -> dict:
            return {
                "g": "group"
            }

    @staticmethod
    def create_group(dto: GroupDto):
        group = dto.group
        # todo: validate group
        g_json = JsonFormatter.serialize(group)
        CacheItemManager.add(EntityType.group, g_json)

    @staticmethod
    def delete_group():
        pass

    @staticmethod
    def update_group():
        pass

    @staticmethod
    def init(_handler):
        _handler["CreateGroup"] = GroupManager.create_group
        _handler["DeleteGroup"] = GroupManager.delete_group
        _handler["UpdateGroup"] = GroupManager.update_group
