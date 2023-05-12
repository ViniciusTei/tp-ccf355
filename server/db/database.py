import sqlite3
import os

class DB:
    def __init__(self) -> None:
         dbUrlLocation = os.getcwd() + '/server/db/sqlite.db'
         self.db = sqlite3.connect(dbUrlLocation)
    pass