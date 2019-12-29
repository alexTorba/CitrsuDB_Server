from abc import ABCMeta, abstractmethod

from Entities.EntityType import EntityType


class EntityDAO(metaclass=ABCMeta):

    @property
    @abstractmethod
    def entity_type(self) -> EntityType:
        pass

    @property
    def table_name(self) -> str:
        return str(self.entity_type).split(".")[1].capitalize()

    @abstractmethod
    def try_initialize(self):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def read(self, Id):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def update(self, Id, data):
        pass

    @abstractmethod
    def delete(self, Id):
        pass
