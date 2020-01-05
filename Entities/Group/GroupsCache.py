from typing import Dict

from Common.Cache.BaseCache import BaseCache
from Entities.EntityType import EntityType
from Entities.Group.GroupContext import GroupContext


class GroupsCache(BaseCache[GroupContext]):

    def __init__(self, cacheItems: Dict[int, GroupContext] = None) -> None:
        super().__init__(cacheItems)

    def get_type_cache(self) -> EntityType:
        return EntityType.group
