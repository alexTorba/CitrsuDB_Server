from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Dict

from Common.Entity.BaseEntityContext import BaseEntityContext
from Entities.EntityType import EntityType

T = TypeVar("T", BaseEntityContext, object)


class BaseCache(Generic[T], ABC):
    _cacheItems: Dict[int, T] = dict()  # key - id of entity, value - Context

    def __init__(self, cacheItems: Dict[int, T] = None) -> None:
        if cacheItems is not None:
            self._cacheItems.update(cacheItems)

    def add(self, id_entity: int, entity_context: T) -> None:
        self._cacheItems[id_entity] = entity_context

    def get(self, id_entity: int) -> T:
        return self._cacheItems.get(id_entity)

    def update(self, id_entity: int, entity_context: T) -> None:
        self._cacheItems[id_entity] = entity_context

    def remove(self, id_entity: int) -> None:
        self._cacheItems.pop(id_entity)

    @abstractmethod
    def get_type_cache(self) -> EntityType:
        pass
