from Common.JsonFormatter.JsonFormatter import JsonFormatter
from Common.JsonFormatter.JsonTest.TestEntities.City import City
from Entities.Group.Group import Group
from Entities.Student.Student import Student


class JsonTest:

    @staticmethod
    def test_city():
        c = City.get_test()
        c_json = JsonFormatter.serialize(c)
        c_val: City = JsonFormatter.deserialize(c_json, City)
        print()

    @staticmethod
    def test_group():
        g = Group.get_test_group()
        g_json = JsonFormatter.serialize(g)
        g_Val = JsonFormatter.deserialize(g_json, Group)
        print()

    @staticmethod
    def test_student():
        s = Student.get_test_student()
        s_json = JsonFormatter.serialize(s)
        s_val = JsonFormatter.deserialize(s_json, Student)
        print()
