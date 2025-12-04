import sys
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from outcome_prediction.logger.log import logging
from outcome_prediction.exception.exception_handler import AppException

class TargetValueMapping:
    def __init__(self):
        self.Certified:int = 0
        self.Denied:int = 1

    def _asdict(self):
        return self.__dict__
    
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))


class PrepareModel:
    def __init__(self, preprocessing_object: Pipeline, trained_model_object: object):
        """
        :param preprocessing_object: Input Object of preprocesser
        :param trained_model_object: Input Object of trained model 
        """
        try:
            self.preprocessing_object = preprocessing_object
            self.trained_model_object = trained_model_object
        except Exception as e:
            raise AppException(e, sys) from e 

    def predict(self, dataframe: DataFrame)->DataFrame:
        """
        Function accepts raw inputs and then transformes raw input using preprocessing_object
        which guarantees that the inputs are in the same format as the training data
        it performs prediction on transformed features
        """
        try:
            transformed_feature = self.preprocessing_object.transform(dataframe)

            return self.trained_model_object.predic(transformed_feature)

        except Exception as e:
            raise AppException(e, sys) from e 

    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"
    
    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"