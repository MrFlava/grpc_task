from dotenv import dotenv_values

from db import MongoDbConnector

config = dotenv_values(".env")

def mongo_connector() -> MongoDbConnector:
    return MongoDbConnector(host=config["MONGO_HOST"], port=int(config["MONGO_PORT"]))