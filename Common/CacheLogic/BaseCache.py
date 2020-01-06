from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Dict

from Common.Entity.BaseEntity import BaseEntity
from Entities.EntityType import EntityType

T = TypeVar("T", bound=BaseEntity)


class BaseCache(Generic[T], ABC):
    _cacheItems: Dict[int, T] = dict()  # key - id of entity, value - Entity

    def __init__(self, cacheItems: Dict[int, T] = None) -> None:
        if cacheItems is not None:
            self._cacheItems.update(cacheItems)

    def add(self, id_entity: int, entity: T) -> None:
        self._cacheItems[id_entity] = entity

    def get(self, id_entity: int) -> T:
        return self._cacheItems.get(id_entity)

    def update(self, id_entity: int, entity: T) -> None:
        self._cacheItems[id_entity] = entity

    def remove(self, id_entity: int) -> None:
        self._cacheItems.pop(id_entity)

    @abstractmethod
    def get_type_cache(self) -> EntityType:
        pass
