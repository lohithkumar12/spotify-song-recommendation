from spotify_recommendation.config.configuration import ConfigurationManager
from spotify_recommendation.components.data_transformation import DataTransformation
from spotify_recommendation.logging import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        """Runs data transformation pipeline"""
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        cleaned_data_path = data_transformation.transform_data()
        logger.info(f"Data Transformation completed! Cleaned data saved at {cleaned_data_path}")

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
