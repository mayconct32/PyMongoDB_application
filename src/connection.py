from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from config import config

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            config["username"],
            config["password"],
            config["host"],
            config["port"]
        )
        self.__database_name = config["db_name"]
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        self.__client = AsyncMongoClient(self.__connection_string,timeoutMS=100000)
        self.__db_connection = self.__client[self.__database_name]
    
    def get_db_connection(self) -> AsyncDatabase:
        if not self.__db_connection:
            self.connect_to_db()
        return self.__db_connection