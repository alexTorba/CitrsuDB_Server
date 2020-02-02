from datetime import datetime
from typing import List, Dict

from Common.JsonLogic.JsonFormatter import JsonFormatter
from Common.JsonLogic.JsonTest.TestEntities.City import City
from Common.JsonLogic.JsonTest.TestEntities.Univercity.University import University
from Common.JsonLogic.TypeInspect import TypeInspect
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
        for i in range(0,9):
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
    def json_speed_test():
        entity_count = 10
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
        start_time = datetime.now()
        university_json = JsonFormatter.serialize(university)
        university_val = JsonFormatter.deserialize(university_json, University)
        stop_time = datetime.now()
        delta = stop_time - start_time
        return delta.total_seconds() * 1000

    @staticmethod
    def json_speed_average_test(iterations):
        count = 0
        for i in range(0, iterations):
            count += JsonTest.json_speed_test()
        print(count / iterations)

    @staticmethod
    def test_annotations():
        my_dict: Dict[type, dict] = dict()
        my_dict[Student] = {"a": str}
        if Student in my_dict:
            print("+")
        print()


JsonTest.json_speed_average_test(20)
