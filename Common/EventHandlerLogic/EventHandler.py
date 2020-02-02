import pkgutil
from dis import dis
from typing import TypeVar, Generic, List

from Common.EventHandlerLogic.IEventHandler import IEventHandler

T = TypeVar("T", bound=IEventHandler)


class EventHandler(Generic[T]):
    data: List[T] = list()

    @classmethod
    def add(cls, data: T):
        cls.data.append(data)

    @classmethod
    def show(cls):
        for i in cls.data:
            print(i)


class FirstObserver(IEventHandler):

    def invoke(self):
        pass


class SecondObserver(IEventHandler):

    def invoke(self):
        pass


def test1():
    my_list = [1, 0, False, True, "", "A"]
    filtered_data = [i for i in my_list if i]
    for i in filtered_data:
        print(i)


def test2():
    my_list = [1, 0, False, True, "", "A"]
    filtered_data = []
    for i in my_list:
        if i:
            filtered_data.append(i)

    for i in filtered_data:
        print(i)


print(dis(test1))
print("\n____________________________________________________\n")
print(dis(test2))
