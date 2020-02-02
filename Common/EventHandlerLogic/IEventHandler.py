from abc import ABC, abstractmethod


class IEventHandler(ABC):
    @abstractmethod
    def invoke(self):
        pass
