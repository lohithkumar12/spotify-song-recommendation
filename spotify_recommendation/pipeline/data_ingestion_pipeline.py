from spotify_recommendation.config.configuration import ConfigurationManager
from spotify_recommendation.components.data_ingestion import DataIngestion
from spotify_recommendation.logging import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        """Runs the data ingestion process."""
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            # Check if dataset exists
            data_ingestion.download_file()

            # Load dataset
            df = data_ingestion.load_data()

            logger.info(f"Data Ingestion completed successfully! Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
            return df
        except Exception as e:
            logger.exception(f"Error in Data Ingestion: {str(e)}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
