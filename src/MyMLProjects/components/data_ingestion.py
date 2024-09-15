import os
from src.MyMLProjects.logger import logging
from src.MyMLProjects.exception import CustomException
import sys
import pandas as pd
from src.MyMLProjects.utils import red_mysql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConig:
    train_data_set = os.path.join('artifacts','train_data.csv')
    test_data_set = os.path.join('artifacts','test_data.csv')
    raw_data_set = os.path.join('artifacts','raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConig()

    def Init_data_ingestion(self):
        try:
            
            df=red_mysql_data()
            logging.info("reading data from MySql")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_set),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_set,index=False,header=True)

            train_set,test_set =train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_set,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_set,index=False,header=True)
            logging.info("Datainjection completed")
            return(
                self.ingestion_config.train_data_set,
                self.ingestion_config.test_data_set
            )
        except Exception as e:
            raise CustomException(e,sys)

        
