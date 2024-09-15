from src.MyMLProjects.logger import logging
from src.MyMLProjects.exception import CustomException
from src.MyMLProjects.components.data_ingestion import DataIngestion
import sys

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.Init_data_ingestion()

    except Exception as e:
         logging.info("Custom Exception")
         raise CustomException(e,sys)    
