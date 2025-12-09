from outcome_prediction.configuration.mongo_db_connection import MongoDBClient
from outcome_prediction.constants import DATABASE_NAME
from outcome_prediction.exception.exception_handler import AppException

import pandas as pd
import sys
from typing import Optional
import numpy as np



class PrepareData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """
    def __init__(self):
        try:
            
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

            print(f"connected to mongo db: {DATABASE_NAME}")
        except Exception as e:
            raise AppException(e, sys) from e
        
    def export_collection_to_dataframe(self, collection_name:str, database_name:Optional[str]=None)->pd.DataFrame:
        """
        export entire collectin as dataframe:
        return pd.DataFrame of collection
        """
        try:
            
            # Connect to the database
            db = self.mongo_client.database

            # Example operation: Fetch documents from a collection
            collection = db[collection_name]
        
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis = 1)
            df.replace({"na": np.nan}, inplace= True )

            return df 
        except Exception as e:
            raise AppException(e, sys) from e 
            
