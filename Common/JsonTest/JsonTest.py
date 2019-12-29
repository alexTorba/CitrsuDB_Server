from Common.JsonFormatter import JsonFormatter
from Common.JsonTest.TestEntities.City import City
from Entities.Group import Group


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
