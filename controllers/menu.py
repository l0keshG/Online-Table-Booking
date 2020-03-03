from utils_test import connectToDb
from sql_scripts.select_scripts import menus

cur = connectToDb()
def get_menu_data():

    cur.execute(menus)
    data = cur.fetchall()
    return data