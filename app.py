from src.MyMLProjects.logger import logging
from src.MyMLProjects.exception import CustomException
from src.MyMLProjects.components.data_ingestion import DataIngestion
from src.MyMLProjects.components.data_transformation import DataTransformation
import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.Init_data_ingestion()
        train_data_path,test_data_path=data_ingestion.Init_data_ingestion()
        data_transformation=DataTransformation()
        #data_transformation.initiate_data_transormation(train_data_path,test_data_path)
   
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)  
