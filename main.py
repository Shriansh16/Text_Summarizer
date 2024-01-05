import os
import sys
from src.logger import *
from src.exception import *
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f"{STAGE_NAME} STARTED")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f"{STAGE_NAME} COMPLETED")
except Exception as e:
    logging.info("ERROR OCCURED IN DATA INGESTION")
    raise CustomException(e,sys)
