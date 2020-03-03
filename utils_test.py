import psycopg2
from settings import config
import logging

logging.basicConfig(filename="newfile.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w',
					level=logging.INFO)
log = logging.getLogger()

def connectToDb():


    connection = psycopg2.connect(user="postgres",
                                        password="postgres",
                                        host="localhost",
                                        database="postgres")
    connection.autocommit = True
    cursor = connection.cursor()

    return cursor