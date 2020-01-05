from abc import ABC
from typing import Generic, TypeVar

from Common.Entity.BaseEntity import BaseEntity
from DataBaseLogic.DBManager import DBManager
from Entities.EntityType import EntityType

T = TypeVar("T", bound=BaseEntity)


class BaseEntityContext(Generic[T], ABC):
    __isDirty: bool = False
    _entity: T
    __db: DBManager

    def read(self) -> T:
        return self._entity

    def edit(self) -> T:
        self.__isDirty = True
        return self._entity

    def is_dirty(self) -> bool:
        return self.__isDirty

    def __init__(self, entity: T = None, db: DBManager = None) -> None:
        if entity is not None:
            self._entity = entity
        self.__isDirty = False
        self.__db = db

    def save(self):
        if self.__isDirty:
            entity_type = self.get_entity_type()
            self.__db.update(entity_type, self._entity.id, self._entity.data)
            self.__isDirty = False

    def get_entity_type(self) -> EntityType:
        return self._entity.entity_type
