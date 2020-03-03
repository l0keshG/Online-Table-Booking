from utils import connectToDb
from sql_scripts.select_scripts import tables

cur = connectToDb()
def get_table_data():

    cur.execute(tables)
    data = cur.fetchall()
    return data