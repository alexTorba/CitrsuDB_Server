from typing import List

from Common.Cache.BaseCache import BaseCache
from Common.Entity.BaseEntityContext import BaseEntityContext
from DataBaseLogic.DBManager import DBManager
from Entities.EntityType import EntityType
from Entities.Group.GroupsCache import GroupsCache
from Entities.Student.StudentsCache import StudentsCache
from Modules.ContextFactory import ContextFactory


class CacheItemManager:
    __cache_items: List[BaseCache] = [GroupsCache(), StudentsCache()]
    __db: DBManager = DBManager()

    @classmethod
    def _get_appropriate_cache(cls, entity_type: EntityType) -> BaseCache:
        return [c for c in cls.__cache_items if c.get_type_cache() is entity_type][0]

    @classmethod
    def init_cache(cls):
        for c in cls.__cache_items:
            entity_type: EntityType = c.get_type_cache()
            items: (int, str) = cls.__db.read_all(entity_type)
            for i in items:
                context = ContextFactory.create_context(entity_type, i[1])
                c.add(i[0], context)

    @classmethod
    def add(cls, entity_type: EntityType, entity_json: str) -> BaseEntityContext:
        cache = cls._get_appropriate_cache(entity_type)
        new_context = ContextFactory.create_context(entity_type, entity_json)
        entity_id = new_context.read().id
        if cache.get(entity_id) is None:
            cache.add(entity_id, new_context)
            cls.__db.create(entity_type, entity_json)
        return new_context

    @classmethod
    def remove(cls, entity_type: EntityType, entity_id: int):
        cache = cls._get_appropriate_cache(entity_type)
        cache.remove(entity_id)
        cls.__db.delete(entity_type, entity_id)

    @classmethod
    def get(cls, entity_type: EntityType, entity_id: int) -> BaseEntityContext:
        cache = cls._get_appropriate_cache(entity_type)
        cx = cache.get(entity_id)
        if cx is None:
            (entity_id, json) = cls.__db.read(entity_type, entity_id)
            cx = cls.add(entity_type, json)
        return cx
