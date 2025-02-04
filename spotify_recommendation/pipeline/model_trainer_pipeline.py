from spotify_recommendation.config.configuration import ConfigurationManager
from spotify_recommendation.components.model_trainer import ModelTrainer
from spotify_recommendation.logging import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        """Runs the model training pipeline."""
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)

            # Train the model
            model_trainer.train_model()

            logger.info(f"Model Training completed successfully!")
        except Exception as e:
            logger.exception(f"Error in Model Training: {str(e)}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
