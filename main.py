import inspect
import typing
from abc import ABCMeta, ABC

from Common.JsonFormatter.JsonContract import JsonContract
from Common.JsonFormatter.JsonFormatter import JsonFormatter
from Common.JsonFormatter.JsonTest.JsonTest import JsonTest
from Common.JsonFormatter.TypeInspect import TypeInspect
from Entities.Student.Student import Student
from Entities.Student.StudentData import StudentData

T = typing.TypeVar("T", bound=JsonContract)


class BaseClass(typing.Generic[T]):
    field: T

    def __init__(self, field: T = None) -> None:
        if field is not None:
            self.field = field


class DerivedClass(BaseClass[StudentData]):
    pass


def test():
    JsonTest.test_student()
    JsonTest.test_group()
    print()


def main():
    test()


if __name__ == '__main__':
    main()
