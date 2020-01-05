from typing import Dict

from Common.Cache.BaseCache import BaseCache
from Entities.EntityType import EntityType
from Entities.Student.StudentContext import StudentContext


class StudentsCache(BaseCache[StudentContext]):

    def __init__(self, cacheItems: Dict[int, StudentContext] = None) -> None:
        super().__init__(cacheItems)

    def get_type_cache(self) -> EntityType:
        return EntityType.student
