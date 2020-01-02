from abc import ABCMeta, abstractmethod

from Common.JsonFormatter.JsonContract import JsonContract
from Entities.EntityType import EntityType


class IEntity:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def Id(self) -> int:
        pass

    @property
    @abstractmethod
    def data(self) -> JsonContract:
        pass

    @property
    @abstractmethod
    def entity_type(self) -> EntityType:
        pass
