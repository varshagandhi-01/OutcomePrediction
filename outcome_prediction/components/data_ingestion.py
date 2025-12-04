import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split

from outcome_prediction.logger.log import logging
from outcome_prediction.exception.exception_handler import AppException
from outcome_prediction.data_access.prepare_data import PrepareData
from outcome_prediction.entity.artifact_entity import DataIngestionArtifact
from outcome_prediction.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, data_ingestion_config = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys) from e 

    def export_data_into_feature_store(self) -> DataFrame:
        try:
            logging.info("Exporting data from mongodb to data frame")
            raw_data = PrepareData()
            dataframe = raw_data.export_collection_to_dataframe(collection_name = self.data_ingestion_config.collection_name)
            logging.info(f"shape of dataframe : {dataframe.shape}")

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Saving export dataframe at : {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            
            return dataframe

        except Exception as e:
            raise AppException(e, sys) from e 
        

    def split_data_as_train_test(self, dataframe: DataFrame)->None:
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)

            # save train and test datasets as csv files
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Exporting train and test files")

            train_set.to_csv(self.data_ingestion_config.training_file_path, index = False, header = True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index = False, header = True)

            logging.info(f"Exported train and test files")

        except Exception as e:
            raise AppException(e, sys) from e 
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe)

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path, 
            test_file_path=self.data_ingestion_config.testing_file_path)

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys) from e 