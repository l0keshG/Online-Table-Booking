from utils_test import connectToDb
from sql_scripts.select_scripts import restaurant

cur = connectToDb()
def get_restaurants():

    cur.execute(restaurant)
    data = cur.fetchall()
    return data

