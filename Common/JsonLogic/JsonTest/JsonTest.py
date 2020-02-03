from datetime import datetime
from typing import List, Callable

import git

from Common.JsonLogic.JsonFormatter import JsonFormatter
from Common.JsonLogic.JsonTest.TestEntities.City import City
from Common.JsonLogic.JsonTest.TestEntities.Univercity.University import University
from Entities.Group.Group import Group
from Entities.Group.GroupData import GroupData
from Entities.Student.Student import Student
from Entities.Student.StudentData import StudentData


class JsonTest:

    @staticmethod
    def test_city():
        c = City.get_test_city()
        c_json = JsonFormatter.serialize(c)
        c_val: City = JsonFormatter.deserialize(c_json, City)
        print()

    @staticmethod
    def test_group():
        students: List[StudentData] = list()
        for i in range(0, 9):
            student = Student.get_test_student()
            students.append(student.data)

        g = Group.get_test_group()
        g.data.Students = students
        g_json = JsonFormatter.serialize(g)
        g_Val = JsonFormatter.deserialize(g_json, Group)
        print()

    @staticmethod
    def test_student():
        s = Student.get_test_student()
        s_json = JsonFormatter.serialize(s)
        s_val = JsonFormatter.deserialize(s_json, Student)
        print()

    @staticmethod
    def get_large_university(entity_count: int) -> University:
        students: List[StudentData] = list()
        for i in range(0, entity_count):
            student = Student.get_test_student()
            students.append(student.data)

        groups: List[GroupData] = list()
        for i in range(0, entity_count):
            group: Group = Group.get_test_group()
            group.data.Students = students
            groups.append(group.data)

        university: University = University.get_test_university()
        university.data.groups = groups

        return university

    @staticmethod
    def json_generic_speed_test(entity_count: int) -> float:
        university = JsonTest.get_large_university(entity_count)
        start_time = datetime.now()
        university_json = JsonFormatter.serialize(university)
        university_val = JsonFormatter.deserialize(university_json, University)
        stop_time = datetime.now()
        delta = stop_time - start_time
        return delta.total_seconds() * 1000

    @staticmethod
    def json_serializations_test(entity_count: int) -> float:
        university = JsonTest.get_large_university(entity_count)
        start_time = datetime.now()
        university_json = JsonFormatter.serialize(university)
        stop_time = datetime.now()
        return (stop_time - start_time).total_seconds() * 1000

    @staticmethod
    def json_deserialization_test(entity_count: int) -> float:
        university = JsonTest.get_large_university(entity_count)
        university_json = JsonFormatter.serialize(university)
        start_time = datetime.now()
        university_val = JsonFormatter.deserialize(university_json, University)
        stop_time = datetime.now()
        delta = stop_time - start_time
        return delta.total_seconds() * 1000

    @staticmethod
    def json_speed_average_test(iterations: int, entity_count: int, test_func: Callable[[int], float]) -> float:
        result = 0
        for i in range(0, iterations):
            result += test_func(entity_count)
        return result / iterations

    @staticmethod
    def json_speed_test():
        entity_count = 50
        iterations = 20

        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha

        data_to_write = ""
        data_to_write += f"Last commit {sha}\n"
        data_to_write += f"JsonFormatter test. Entity count = {entity_count}, Count of iterations = {iterations}\n"

        average_speed = JsonTest.json_speed_average_test(iterations, entity_count, JsonTest.json_serializations_test)
        data_to_write += f"Serializations : {average_speed}ms\n"

        average_speed = JsonTest.json_speed_average_test(iterations, entity_count, JsonTest.json_deserialization_test)
        data_to_write += f"Deserialization : {average_speed}ms\n"

        average_speed = JsonTest.json_speed_average_test(iterations, entity_count, JsonTest.json_generic_speed_test)
        data_to_write += f"Generic average : {average_speed}ms\n\n"

        print(data_to_write)
        # JsonTest.write_result(data_to_write)
        # print("write result success !")

    @staticmethod
    def write_result(data: str) -> None:
        with open("JsonTest.txt", "a") as file:
            file.write(data)


JsonTest.json_speed_test()
