from spotify_recommendation.logging import logger
from spotify_recommendation.pipeline.data_ingestion_pipeline import DataUpdatePipeline
from spotify_recommendation.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from spotify_recommendation.pipeline.data_transformation_pipeline import DataTransformationPipeline
from spotify_recommendation.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from spotify_recommendation.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    
    data_ingestion = DataUpdatePipeline(
        client_id="f2e62d2b58e044bba3529a391565da78",
        client_secret="4125a139a17c465b93a166b13d9f4ad3",
        playlist_id="5fCbYbykLg85EVHHYrkgLw"
    )
    
    data_ingestion.initiate_data_update()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
