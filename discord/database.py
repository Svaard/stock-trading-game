import pymongo
import config

class Database():
    CLIENT = None
    DATABASE = None

    @staticmethod
    def initialize():
        Database.CLIENT = pymongo.MongoClient(config.CONNECTION_STRING)
        Database.DATABASE = Database.CLIENT['stonks']
        print(f'\n { Database.DATABASE } connection initialized. \n')

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def close():
        Database.CLIENT.close()
        print(f'\n { Database.DATABASE } connection closed. \n')