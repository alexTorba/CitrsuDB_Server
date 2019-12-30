from abc import ABCMeta, abstractmethod
from sqlite3 import Cursor
from Entities.EntityType import EntityType


class EntityDAO(metaclass=ABCMeta):

    _cursor: Cursor
    __create_table: str = """CREATE TABLE IF NOT EXISTS [{table_name}] ([Id] INTEGER PRIMARY KEY AUTOINCREMENT, [Data] TEXT NOT NULL)"""

    __create_query: str = """INSERT INTO [{table_name}] ([Data]) VALUES (?)"""

    __read_query: str = """SELECT Data FROM [{table_name}] WHERE [Id] = {Id}"""

    __read_all_query: str = """SELECT * FROM [{table_name}]"""

    __update_query: str = """UPDATE [{table_name}] SET [Data] = {data} WHERE [Id] = {Id}"""

    __delete_query: str = """DELETE FROM [{table_name}] WHERE [Id] = {Id}"""

    @property
    @abstractmethod
    def entity_type(self) -> EntityType:
        pass

    @abstractmethod
    def __init__(self, cursor: Cursor) -> None:
        self._cursor = cursor

    @property
    def table_name(self) -> str:
        return str(self.entity_type).split(".")[1].capitalize()

    def try_initialize(self):
        query: str = self.__create_table.format(table_name=self.table_name)
        self._cursor.execute(query)

    def create(self, data):
        query: str = self.__create_query.format(table_name=self.table_name)
        self._cursor.execute(query, (data,))

    def read(self, Id):
        query: str = self.__read_query.format(
            table_name=self.table_name, Id=Id)
        self._cursor.execute(query)

    def read_all(self):
        query: str = self.__read_all_query.format(table_name=self.table_name)
        self._cursor.execute(query)

    def update(self, Id, data):
        query: str = self.__update_query.format(
            table_name=self.table_name, data=data, Id=Id)
        self._cursor.execute(query)

    def delete(self, Id):
        query: str = self.__delete_query.format(
            table_name=self.table_name, Id=Id)
        self._cursor.execute(query)
