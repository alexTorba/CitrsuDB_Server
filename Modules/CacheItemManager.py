from typing import List, cast

from Common.Cache.BaseCache import BaseCache
from Common.Entity.BaseEntity import BaseEntity
from Common.JsonFormatter.JsonFormatter import JsonFormatter
from DataBaseLogic.DBManager import DBManager
from Entities.EntityFactory import EntityFactory
from Entities.EntityType import EntityType
from Entities.Group.GroupsCache import GroupsCache
from Entities.Student.StudentsCache import StudentsCache


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
            for entity_id, data in items:
                entity = EntityFactory.create_entity(entity_type, data)
                c.add(entity_id, entity)

    @classmethod
    def add(cls, entity_type: EntityType, entity):
        cache = cls._get_appropriate_cache(entity_type)
        if entity is str:
            entity_id = cls.__db.create(entity_type, entity)  # id from db autoincrement key
            new_entity = EntityFactory.create_entity(entity_type, entity)
            new_entity.id = entity_id
            cache.add(entity_id, new_entity)
        elif entity is BaseEntity:
            entity = cast(BaseEntity, entity)
            entity_json = JsonFormatter.serialize(entity)
            entity_id = cls.__db.create(entity_type, entity_json)  # id from db autoincrement key
            if cache.get(entity_id) is None:
                cache.add(entity_id, entity)

    @classmethod
    def remove(cls, entity_type: EntityType, entity_id: int):
        cache = cls._get_appropriate_cache(entity_type)
        cache.remove(entity_id)
        cls.__db.delete(entity_type, entity_id)

    @classmethod
    def get(cls, entity_type: EntityType, entity_id: int) -> BaseEntity:
        cache = cls._get_appropriate_cache(entity_type)
        entity = cache.get(entity_id)
        if entity is None:
            (entity_id, json) = cls.__db.read(entity_type, entity_id)
            cls.add(entity_type, json)
        return entity
