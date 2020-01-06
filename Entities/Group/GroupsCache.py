from typing import Dict

from Common.Cache.BaseCache import BaseCache
from Entities.EntityType import EntityType
from Entities.Group.Group import Group


class GroupsCache(BaseCache[Group]):

    def __init__(self, cacheItems: Dict[int, Group] = None) -> None:
        super().__init__(cacheItems)

    def get_type_cache(self) -> EntityType:
        return EntityType.group
