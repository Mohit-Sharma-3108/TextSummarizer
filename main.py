from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage: {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.inititate_data_transformation()
    logger.info(f"Stage: {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.inititate_model_trainer()
    logger.info(f"Stage: {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"Stage: {STAGE_NAME} initiated")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.inititate_model_evaluation()
    logger.info(f"Stage: {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e