from spotify_recommendation.config.configuration import ConfigurationManager
from spotify_recommendation.components.model_evaluation import ModelEvaluation
from spotify_recommendation.logging import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        """Runs the model evaluation pipeline."""
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluator = ModelEvaluation(config=model_evaluation_config)

            # Run evaluation
            model_evaluator.run_evaluation()

            logger.info(f" Model Evaluation completed successfully!")
        except Exception as e:
            logger.exception(f" Error in Model Evaluation: {str(e)}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
