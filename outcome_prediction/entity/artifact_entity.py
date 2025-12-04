from dataclasses import dataclass

@dataclass(frozen = True)
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str 

@dataclass(frozen = True)
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str

@dataclass(frozen = True)
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass(frozen = True)
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float

@dataclass(frozen = True)
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact

@dataclass(frozen = True)
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str

@dataclass(frozen = True)
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str