from sqlite3 import Cursor

from DataBaseLogic.EntitiesDAO.EntityDAO import EntityDAO
from Entities.EntityType import EntityType


class GroupDAO(EntityDAO):
    __cursor: Cursor
    __create_table: str = """CREATE TABLE IF NOT EXISTS [{table_name}] ([Id] INTEGER PRIMARY KEY AUTOINCREMENT, [Data] TEXT NOT NULL)"""

    __create_query: str = """INSERT INTO [{table_name}] ([Data]) VALUES (?)"""

    __read_query: str = """SELECT Data FROM [{table_name}] WHERE [Id] = {Id}"""

    __read_all_query: str = """SELECT * FROM [{table_name}]"""

    __update_query: str = """UPDATE [{table_name}] SET [Data] = {data} WHERE [Id] = {Id}"""

    __delete_query: str = """DELETE FROM [{table_name}] WHERE [Id] = {Id}"""

    @property
    def entity_type(self) -> EntityType:
        return EntityType.group

    def __init__(self, cursor: Cursor) -> None:
        self.__cursor = cursor

    def try_initialize(self):
        query: str = self.__create_table.format(table_name=self.table_name)
        self.__cursor.execute(query)

    def create(self, data):
        query: str = self.__create_query.format(table_name=self.table_name)
        self.__cursor.execute(query, (data,))

    def read(self, Id):
        self.__cursor.execute(self.__read_query.format(table_name=self.table_name, Id=Id))

    def read_all(self):
        self.__cursor.execute(self.__read_all_query.format(table_name=self.table_name))

    def update(self, Id, data):
        self.__cursor.execute(self.__update_query.format(table_name=self.table_name, data=data, Id=Id))

    def delete(self, Id):
        self.__cursor.execute(self.__delete_query.format(table_name=self.table_name, Id=Id))
