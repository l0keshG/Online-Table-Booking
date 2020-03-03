from utils_test import connectToDb
from sql_scripts.select_scripts import menus, tables
from sql_scripts.insert_script import order_insert

cur = connectToDb()

def post_order_details(req):
    req = req.json()
    menu_id = req.get("menu_id")
    res_id = req.get("restaurant_id")
    table_id = req.get("table_id")
    user_id = req.get("user_id")

    data = (menu_id, user_id, res_id, table_id)

    flag = check_table_availability_status(table_id)

    if flag == True:
        cur.execuete(order_insert, data)
        cur.commit()
        return "The order has been taken"
    else:
        return "The selected table already reserved. Please select the other table please"

def check_table_availability_status(table_id):

    cur.execuete(tables)
    table_data = cur.fetchall()
    for table in table_data:
        if table[0] == table_id and table[4] == False:
            return True

    return False






