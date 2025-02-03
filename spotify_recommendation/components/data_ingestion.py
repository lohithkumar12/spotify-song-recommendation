import os
import pandas as pd
from spotify_recommendation.logging import logger
from spotify_recommendation.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Checks if the dataset exists and logs the status."""
        if not os.path.exists(self.config.dataset_path):
            raise FileNotFoundError(f"Dataset file not found: {self.config.dataset_path}")
        logger.info(f"Dataset file found: {self.config.dataset_path}")

    def load_data(self):
        """Loads the dataset into a Pandas DataFrame."""
        try:
            df = pd.read_csv(self.config.dataset_path)
            logger.info(f" Successfully loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
            return df
        except Exception as e:
            logger.exception(f"Error loading dataset: {str(e)}")
            raise e
