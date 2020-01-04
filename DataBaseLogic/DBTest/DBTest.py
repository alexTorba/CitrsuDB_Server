from Entities.Group.Group import Group
from DataBaseLogic.DBManager import DBManager
from Common.JsonFormatter.JsonFormatter import JsonFormatter
from Entities.EntityType import EntityType


class DBTest:
    @staticmethod
    def test():
        group = Group.get_test_group()
        db = DBManager()
        json_group = JsonFormatter.serialize(group)
        db.create(EntityType.group, json_group)

        json_group = db.read(EntityType.group, 1)[0]
        group_val = JsonFormatter.deserialize(json_group, Group)
        print()
