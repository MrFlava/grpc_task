from pymongo import MongoClient

class MongoDbConnector:
    def __init__(self, host: str, port: int):
        self.client = MongoClient(host, port)

    def connect(self, db_name: str):
        return self.client[db_name]
