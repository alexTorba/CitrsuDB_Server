import sqlite3


class DBManager:
    def try_initialize(self):
        conn = sqlite3.connect("CitrusDB.db")
