from spotify_recommendation.config.configuration import ConfigurationManager
from spotify_recommendation.components.data_ingestion import SpotifyDataIngestion
from spotify_recommendation.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from spotify_recommendation import logger
import os

STAGE_NAME = "Spotify Data Ingestion & Model Retraining"

class DataUpdatePipeline:
    def __init__(self, client_id, client_secret, playlist_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.playlist_id = playlist_id

    def initiate_data_update(self):
        try:
            # Fetch new song data
            data_ingestion = SpotifyDataIngestion(self.client_id, self.client_secret)
            new_data_path = data_ingestion.save_data(self.playlist_id)

            # Check if data exists
            if os.path.exists(new_data_path):
                logger.info("New data fetched successfully, initiating model retraining...")
                model_trainer = ModelTrainerPipeline()
                model_trainer.initiate_model_training()
            else:
                logger.warning("No new data fetched. Skipping retraining.")

        except Exception as e:
            logger.exception(e)
            raise e
