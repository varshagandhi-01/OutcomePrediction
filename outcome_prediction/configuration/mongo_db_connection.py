import os 
import sys

from outcome_prediction.exception.exception_handler import AppException
from outcome_prediction.logger.log import logging
from outcome_prediction.constants import MONGODB_URL_KEY, DATABASE_NAME

import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key {MONGODB_URL_KEY} is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAfile = ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("Connected to MongoDB successfully")

        except Exception as e:
            raise AppException(e, sys) from e 

