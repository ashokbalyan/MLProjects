
from dotenv import load_dotenv
load_dotenv()
import os
host=os.getenv("host")
user=os.getenv("username1")
password=os.getenv("password")
db=os.getenv('db')

print('host',host)
print('user',user)
print('db',db)

from src.MyMLProjects.logger import logging
from src.MyMLProjects.exception import CustomException
import sys
import pandas as pd

import pymysql




def red_mysql_data():
    logging.info("Reading Mysql DB")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
    
        logging.info("connection establised",mydb)  
        df = pd.read_sql_query("select * from student",mydb)
        return df
    except Exception as e:
        raise CustomException(e,sys)
