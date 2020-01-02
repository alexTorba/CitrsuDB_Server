from Common.JsonFormatter.JsonFormatter import JsonFormatter
from Common.JsonFormatter.JsonTest.TestEntities.City import City
from Entities.Group import Group
from Entities import Student


class TestJson:

    @staticmethod
    def test_city():
        c = City.get_test()
        c_json = JsonFormatter.dumps(c)
        c_val: City = JsonFormatter.loads(c_json, City)
        print()

    @staticmethod
    def test_group():
        g = Group.get_test_group()
        g_json = JsonFormatter.dumps(g)
        g_Val = JsonFormatter.loads(g_json, Group)
        print()

    @staticmethod
    def test_student():
        s = Student.get_test_student()
        s_json = JsonFormatter.dumps(s)
        JsonFormatter.loads(s_json, Student)
        print()
