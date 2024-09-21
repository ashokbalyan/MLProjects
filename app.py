from src.MyMLProjects.logger import logging
from src.MyMLProjects.exception import CustomException
from src.MyMLProjects.components.data_ingestion import DataIngestion
from src.MyMLProjects.components.data_transformation import DataTransformation
from src.MyMLProjects.components.model_tranier import ModelTrainer
import sys



if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.Init_data_ingestion()
        train_data_path,test_data_path=data_ingestion.Init_data_ingestion()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        model_trainer=ModelTrainer()
        result=model_trainer.initiate_model_trainer(train_arr,test_arr)
        print(result)
   
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)  
