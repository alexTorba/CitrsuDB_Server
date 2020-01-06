from typing import Dict

from Common.Cache.BaseCache import BaseCache
from Entities.EntityType import EntityType
from Entities.Student.Student import Student


class StudentsCache(BaseCache[Student]):

    def __init__(self, cacheItems: Dict[int, Student] = None) -> None:
        super().__init__(cacheItems)

    def get_type_cache(self) -> EntityType:
        return EntityType.student
