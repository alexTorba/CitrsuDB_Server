from typing import Generic, TypeVar, Dict

from Common.Entity.BaseEntityContext import BaseEntityContext

T = TypeVar("T", BaseEntityContext, object)


class BaseCache(Generic[T]):
    _cacheItems: Dict[int, T]  # key - id of entity, value - Context

    def add(self, id_entity: int, entity_context: T) -> None:
        self._cacheItems[id_entity] = entity_context

    def get(self, id_entity: int) -> T:
        return self._cacheItems.get(id_entity)

    def update(self, id_entity: int, entity_context: T) -> None:
        self._cacheItems[id_entity] = entity_context

    def remove(self, id_entity: int) -> None:
        self._cacheItems.pop(id_entity)
