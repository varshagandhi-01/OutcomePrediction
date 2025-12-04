import sys
from outcome_prediction.logger.log import logging
from outcome_prediction.exception.exception_handler import AppException
from outcome_prediction.components.data_ingestion import DataIngestion
from outcome_prediction.components.data_validation import DataValidation

from outcome_prediction.entity.config_entity import (DataIngestionConfig,
                                                     DataValidationConfig,
                                                     DataTransformationConfig,
                                                     ModelTrainerConfig,
                                                     ModelEvaluationConfig,
                                                     ModelPusherConfig
                                                     )

from outcome_prediction.entity.artifact_entity import (DataIngestionArtifact,
                                                       DataValidationArtifact
                                                       )

class TrainingPipeline:
    def __init__(self):
        try:
            self.data_ingestion_config = DataIngestionConfig()
            self.data_validation_config = DataValidationConfig()
            self.data_transformation_config = DataTransformationConfig()
            self.model_trainer_config = ModelTrainerConfig()
            self.model_evaluator_config = ModelEvaluationConfig()
            self.model_pusher_config = ModelPusherConfig()

        except Exception as e:
            raise AppException(e, sys) from e 
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e, sys) from e
        

    def start_data_validation(self, data_ingestion_artifact = DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """    
        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=self.data_validation_config)
           
            data_validation_artifact = data_validation.initiate_data_validation()

            return data_validation_artifact
        
        except Exception as e:
            raise AppException(e, sys) from e 

    # main pipeline function
    def run_pipeline(self, ) -> None:
        """
        This method of TrainPipeline class is responsible for running complete pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            
        except Exception as e:
            raise AppException(e, sys) from e 
             
