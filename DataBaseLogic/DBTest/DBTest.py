from Entities.Group import Group
from DataBaseLogic.DBManager import DBManager
from Common.JsonFormatter import JsonFormatter
from Entities.EntityType import EntityType


class DBTest:
    @staticmethod
    def test():
        group = Group.get_test_group()
        db = DBManager.DBManager()
        json_group = JsonFormatter.dumps(group)
        db.create(EntityType.group, json_group)

        json_group = db.read(EntityType.group, 1)[0]
        group_val = JsonFormatter.loads(json_group, Group)
        print()
