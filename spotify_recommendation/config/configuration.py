from spotify_recommendation.utils.common import read_yaml, create_directories
from spotify_recommendation.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from spotify_recommendation.entity.config_entity import (
    DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
)

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        """Initializes ConfigurationManager by reading config, params, and schema files."""
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Ensure artifacts directory exists
        artifacts_path = self.config.get("artifacts_root", "artifacts/")  # Use default if missing
        create_directories([artifacts_path])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Retrieves data ingestion configurations from config.yaml."""
        config = self.config["data_ingestion"]
        return DataIngestionConfig(
            root_dir=config["root_dir"],
            dataset_path=config["dataset_path"]
        )


