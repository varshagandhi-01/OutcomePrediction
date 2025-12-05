# check Mongo db environement variable
'''
import os

mongo_db_url = os.getenv('MONGODB_URL')
print(mongo_db_url)
'''

# test data ingestion
from outcome_prediction.pipeline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.run_pipeline()

