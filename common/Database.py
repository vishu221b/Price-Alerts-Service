from common import constants
import pymongo
from typing import Dict


class Database:
    URI = constants.DATABASE_URI
    DB = pymongo.MongoClient(URI).get_database(name=constants.DATABASE_NAME)

    @staticmethod
    def insert(collection, data):
        Database.DB[collection].insert(data)

    @staticmethod
    def find(collection, query: Dict) -> list:
        result = Database.DB[collection].find(query)
        return [r for r in result]

    @staticmethod
    def find_one(collection, query: Dict) -> Dict:
        return Database.DB[collection].find_one(query)
