from utils import connectToDb
from sql_scripts.select_scripts import menus, custom_menu

cur = connectToDb()
def get_menu_data():

    cur.execute(menus)
    data = cur.fetchall()
    return data

def custom_menu_details(req):

    req = req.args
    restaurant_id = req.get('restaurant_id')
    table_id = req.get('table_id')

    menu_query = custom_menu.format(restaurant_id, table_id)
    cur.execute(menu_query)
    data = cur.fetchall()
    return data





