from spotify_recommendation.utils.common import read_yaml, create_directories
from spotify_recommendation.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from spotify_recommendation.entity.config_entity import (
    DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, RecommendationConfig
)
import mlflow
import os

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH, schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

        # Set MLflow Tracking URI (use local if testing, remote for Hugging Face)
        #mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
        self.tracking_uri = mlflow.get_tracking_uri()
        print(f"MLflow is tracking experiments at: {self.tracking_uri}")
        

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Retrieves data ingestion configurations from config.yaml."""
        config = self.config["data_ingestion"]
        return DataIngestionConfig(
            root_dir=config["root_dir"],
            dataset_path=config["dataset_path"]
        )
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """Retrieves data validation configurations from config.yaml."""
        config = self.config["data_validation"]
        schema = self.schema["columns"]  # Load expected schema from schema.yaml

        return DataValidationConfig(
            root_dir=config["root_dir"],
            dataset_path=self.config["data_ingestion"]["dataset_path"], 
            status_file=config["status_file"],
            schema=schema
        )
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Retrieves data transformation configurations from config.yaml."""
        config = self.config["data_transformation"]

        return DataTransformationConfig(
            root_dir=config["root_dir"],
            transformed_data=config["transformed_data"],
            raw_data_path=config["raw_data_path"],  
            processed_data_dir=config["processed_data_dir"], 
            song_mapping_path=config["song_mapping_path"]
        )
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """Retrieves model training configurations from config.yaml and params.yaml."""
        config = self.config["model_trainer"]
        params = self.params["model_trainer"]  

        return ModelTrainerConfig(
            root_dir=config["root_dir"],
            model_path=config["model_path"],
            preprocessor_path=config["preprocessor_path"],
            num_clusters=params["num_clusters"]  
        )
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """Retrieves model evaluation configurations from config.yaml."""
        config = self.config["model_evaluation"]
        
        return ModelEvaluationConfig(
            root_dir=config["root_dir"],
            evaluation_report=config["evaluation_report"]
        )
    
    def get_recommendation_config(self) -> RecommendationConfig:
        """Retrieves recommendation system configurations from config.yaml."""
        config = self.config["recommendation_system"]
        
        return RecommendationConfig(
            root_dir=config["root_dir"],
            clustered_data_path=config["clustered_data_path"],
            model_path=config["model_path"]
        )
















