import sqlite3
from typing import List

from DataBaseLogic.EntitiesDAO.EntityDAO import EntityDAO
from DataBaseLogic.EntitiesDAO.GroupDAO import GroupDAO
from DataBaseLogic.EntitiesDAO.StudentDAO import StudentDAO
from Entities.EntityType import EntityType


class DBManager:
    __conn: sqlite3.Connection
    __cursor: sqlite3.Cursor
    __daos: List[EntityDAO]

    def __init__(self) -> None:
        self.__conn = sqlite3.connect("CitrusDB.db")
        self.__cursor = self.__conn.cursor()
        self.__daos = [StudentDAO(self.__cursor), GroupDAO(self.__cursor)]
        self.__try_initialize()

    def __try_initialize(self):
        for i in self.__daos:
            i.try_initialize()
            self.__conn.commit()

    def __get_appropriate_dao(self, entity_type: EntityType) -> EntityDAO:
        return [i for i in self.__daos if i.entity_type == entity_type][0]

    def create(self, entity_type: EntityType, data):
        self.__get_appropriate_dao(entity_type).create(data)
        self.__conn.commit()

    def read(self, entity_type: EntityType, Id):
        self.__get_appropriate_dao(entity_type).read(Id)
        return self.__cursor.fetchone()

    def read_all(self, entity_type: EntityType) -> List:
        self.__get_appropriate_dao(entity_type).read_all()
        return self.__cursor.fetchall()

    def update(self, entity_type: EntityType, Id, Data):
        self.__get_appropriate_dao(entity_type).update(Id, Data)
        self.__conn.commit()

    def delete(self, entity_type: EntityType, Id):
        self.__get_appropriate_dao(entity_type).delete(Id)
        self.__conn.commit()

    def __delattr__(self, name: str) -> None:
        self.__conn.close()
        super().__delattr__(name)
