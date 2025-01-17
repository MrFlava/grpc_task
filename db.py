from pymongo import MongoClient

class MongoDbConnector:
    def __init__(self, host: str, port: int):
        self.client = MongoClient(host, port)

    def connect(self, db_name: str):
        return self.client[db_name]

    def disconnect(self, db_name: str):
        self.client[db_name].close()

    def add_item(self, db_name: str, collection_name: str ,item: dict) -> dict:
        collection = self.connect(db_name)[collection_name]

        item = collection.insert_one(item)

        return {"id": item.inserted_id}