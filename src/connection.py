import os
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            os.getenv("USERNAME"),
            os.getenv("PASSWORD"),
            os.getenv("HOST"),
            os.getenv("PORT")
        )
        self.__database_name = os.getenv("DB_NAME")
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        self.__client = AsyncMongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
    
    def get_db_connection(self) -> AsyncDatabase:
        if not self.__db_connection:
            self.connect_to_db()
        return self.__db_connection
    