from utils import connectToDb
from sql_scripts.select_scripts import user_details

cur = connectToDb()
def get_user_data():

    cur.execute(user_details)
    data = cur.fetchall()
    return data