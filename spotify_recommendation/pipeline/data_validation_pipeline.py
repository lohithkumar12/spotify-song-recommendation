from spotify_recommendation.config.configuration import ConfigurationManager
from spotify_recommendation.components.data_validation import DataValidation
from spotify_recommendation.logging import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        """Runs the data validation process."""
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)

            # Validate dataset
            df = data_validation.validate_data()

            logger.info(f"Data Validation completed successfully! Dataset ready for transformation.")
            return df
        except Exception as e:
            logger.exception(f"Error in Data Validation: {str(e)}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
