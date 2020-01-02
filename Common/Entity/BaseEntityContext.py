from abc import ABCMeta
from typing import Generic, TypeVar

from Common.Entity.IEntity import IEntity
from DataBaseLogic.DBManager import DBManager

T = TypeVar("T", IEntity, object)


class BaseEntityContext(Generic[T]):
    __metaclass__ = ABCMeta
    __isDirty: bool
    _db_manager: DBManager = DBManager()
    entity_data: T

    @property
    def read(self) -> T:
        return self.entity_data

    @property
    def edit(self) -> T:
        self.__isDirty = True
        return self.entity_data

    def save(self) -> None:
        if self.__isDirty:
            self.__isDirty = False
            self._db_manager.update(self.entity_data.entity_type,
                                    self.entity_data.Id,
                                    self.entity_data.data)
