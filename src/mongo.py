from connection import DBConnectionHandler
from bson.objectid import ObjectId
from typing import Dict,List
from pymongo.results import InsertOneResult,InsertManyResult
from pymongo.asynchronous.collection import AsyncCollection

class MongoDBRepository:
    def __init__(
        self, db_connection: DBConnectionHandler, collection_name: str
    ) -> None:
        self.__collection_name = collection_name
        self.__db_connection = db_connection

    def __get_collection(self) -> AsyncCollection:
        """Returns the database collection"""
        conn = self.__db_connection.get_db_connection()
        collection = conn.get_collection(
            self.__collection_name
        )
        return collection

    async def select_many_documents(
        self, filter: Dict, return_options: Dict, order_by: str
    ) -> List[Dict]:
        """
        Returns many documents from the collection.

        Parameters:
            filter (dict): the filter for the query
            return_options (dict): The properties that will be returned
            order_by (str): the property that will be ordered

        Returns:
            List[dict]: data from multiple documents
        """
        collection = self.__get_collection()
        retorno = collection.find(
            filter, 
            return_options 
        ).sort([(order_by,-1)]) 
        response = [c async for c in retorno]
        return response
    
    async def select_one_document(
        self, filter: Dict, return_options: Dict
    ) -> Dict:
        """
        Returns 1 document from the collection,

        Parameters:
            filter (dict): the filter for the query
            return_options (dict): The properties that will be returned
        
        Returns:
            Dict: document data
        """
        collection = self.__get_collection()
        response = await collection.find_one(
            filter,
            return_options
        )
        return response

    async def insert_document(self, data: Dict) -> InsertOneResult:
        """
        Add a document to the collection.

        Parameters:
            data (Dict): data to be entered into the collection

        Returns:
            InsertOneResult -> class containing the identifier of the 
            inserted document
        """
        collection = self.__get_collection()
        return await collection.insert_one(data)
    
    async def insert_list_of_documents(self, data: List[Dict]) -> InsertManyResult:
        """
        Adds several documents to the collection.

        Parameters:
            data (List[Dict]): Documents to be inserted.
        
        Returns:
            InsertManyResult -> class that contains the identifier of the
            inserted documents
        """
        collection = self.__get_collection()
        return await collection.insert_many(data)

    async def select_if_property_exists(self, property: str) -> List[Dict]:
        """
        Select the documents where the property exists.

        Parameters:
            property (str): property to be found in the collection
        
        Returns:
            List[Dict]: list of documents that include the property
        """
        collection = self.__get_collection()
        documents = collection.find(
            {property:{"$exists":True}} 
        )
        response = [doc async for doc in documents]
        return response
        
    async def select_or(self, filter1: Dict, filter2: Dict) -> List[Dict]:
        """
        Returns multiple documents from the collection using filters with
        the logical OR operator.
        
        Parameters:
            filter1 (Dict): first filter for the query
            filter2 (Dict): second filter for the query
        
        Returns:
            List[dict]: data from multiple documents
        """
        collection = self.__get_collection()
        documents = collection.find({"$or":[filter1,filter2]}) 
        response = [doc async for doc in documents]
        return response
    
    async def select_by_id(self, id: str) -> Dict:
        """
        Select the document from the collection by its ID.

        Parameters:
            id (str): the document identifier
        
        Returns:
            Dict: document data
        """
        collection = self.__get_collection()
        response = await collection.find_one({"_id":ObjectId(id)})
        return response 
    
    async def update(self, id: str, data: Dict) -> int:
        """
        Update the collection document.

        Parameters:
            id (str): the document identifier
            data (Dict): data to be changed in the documents
        
        Returns:
            int: number of documents changed
        """
        collection = self.__get_collection()
        response = await collection.update_one(
            {"_id":ObjectId(id)}, 
            {"$set": data} 
        )
        return response.modified_count

    async def update_many(self, filter: Dict, data: Dict) -> int:
        """
        Update the collection documents

        Parameters:
            filter (dict): the filter to update the data
            data (Dict): data to be changed in the documents
        
        Returns:
            int: number of documents changed
        """
        collection = self.__get_collection()
        response = await collection.update_many(
            filter,
            {"$set": data} 
        )
        return response.modified_count 

    async def increases_age(self, id: str) -> int:
        """
        Increases the "age" property of a document using $inc.

        Parameters:
            id (str): the document identifier
        
        Returns:
            int: number of documents changed
        """
        collection = self.__get_collection()
        response = await collection.update_many(
            {"_id":ObjectId(id)},
            {"$inc":{"idade": 3}}
        )
        return response.modified_count

    async def delete(self, id: str) -> int:
        """
        Remove document from collection.

        Parameters:
            id (str): the document identifier

        Returns:
            int: number of deleted documents
        """
        collection = self.__get_collection()
        response = await collection.delete_one(
            {"_id":ObjectId(id)}
        )
        return response.deleted_count
    
    async def delete_many(self, filter: Dict) -> int:
        """
        Remove multiple documents from the collection.

        Parameters:
            filter (Dict): the filter to exclude documents

        Returns:
            int: number of deleted documents
        """
        collection = self.__get_collection()
        response = await collection.delete_many(filter)
        return response.deleted_count


def main():
    # error and exception handling
    # execute methods of the MongoDBRepository
    pass


if __name__ == "__main__":
    main()

