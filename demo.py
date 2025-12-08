# check Mongo db environement variable
'''
import os

mongo_db_url = os.getenv('MONGODB_URL')
print(mongo_db_url)
'''
'''
# test data ingestion
from outcome_prediction.pipeline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.run_pipeline()

'''

from pymongo.mongo_client import MongoClient
import os
uri = os.getenv("MONGODB_URL")
# Create a new client and connect to the server
print(uri)
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)