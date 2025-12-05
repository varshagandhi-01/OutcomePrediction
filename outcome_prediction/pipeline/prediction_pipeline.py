import os
import sys
import numpy as np
import pandas as pd
from pandas import DataFrame
from outcome_prediction.logger.log import logging
from outcome_prediction.exception.exception_handler import AppException
from outcome_prediction.utils.main_utils import read_yaml_file
from outcome_prediction.entity.config_entity import OutcomePredictorConfig
from outcome_prediction.entity.s3_estimator import ModelEstimator

class RawData:
    def __init__(self,
                continent,
                education_of_employee,
                has_job_experience,
                requires_job_training,
                no_of_employees,
                region_of_employment,
                prevailing_wage,
                unit_of_wage,
                full_time_position,
                company_age
                ):
        """
        Raw Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.continent = continent
            self.education_of_employee = education_of_employee
            self.has_job_experience = has_job_experience
            self.requires_job_training = requires_job_training
            self.no_of_employees = no_of_employees
            self.region_of_employment = region_of_employment
            self.prevailing_wage = prevailing_wage
            self.unit_of_wage = unit_of_wage
            self.full_time_position = full_time_position
            self.company_age = company_age
        except Exception as e:
            raise AppException(e, sys) from e
        
    def get_raw_data_frame(self) -> DataFrame:
        try:
            input_dict = self.get_raw_data_as_dict()
            return DataFrame(input_dict)

        except Exception as e:
            raise AppException(e, sys) from e   

    def get_raw_data_as_dict(self):
        try:
            input_data = {
                "continent": [self.continent],
                "education_of_employee": [self.education_of_employee],
                "has_job_experience": [self.has_job_experience],
                "requires_job_training": [self.requires_job_training],
                "no_of_employees": [self.no_of_employees],
                "region_of_employment": [self.region_of_employment],
                "prevailing_wage": [self.prevailing_wage],
                "unit_of_wage": [self.unit_of_wage],
                "full_time_position": [self.full_time_position],
                "company_age": [self.company_age],
            }

            return input_data
        
        except Exception as e:
            raise AppException(e, sys) from e           
        
class DataClassifier:
    def __init__(self, prediction_pipeline_config: OutcomePredictorConfig = OutcomePredictorConfig()) -> None:
        try:
            self.prediction_pipeline_config = prediction_pipeline_config

        except Exception as e:
            raise AppException(e, sys) from e         
        
    def predict(self, dataframe) -> str:
        try:
            model = ModelEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,           
            )

            result = model.predict(dataframe)

            return result
        
        except Exception as e:
            raise AppException(e, sys) from e   