from utils import connectToDb
from sql_scripts.select_scripts import menu_id, tables, orders
from sql_scripts.insert_script import order_insert
import json

cur = connectToDb()

def post_order_details(req):
    
    req = req.json
    menu_id = req.get("menu_id")
    res_id = req.get("restaurant_id")
    table_id = req.get("table_id")
    user_id = req.get("user_id")

    data = (menu_id, user_id, res_id, table_id)

    flag = check_table_availability_status(table_id)

    if flag == True:
        data = cur.execute(order_insert, data)
        return "The order has been taken"
    else:
        return "The selected table already reserved. Please select the other table please"

def check_table_availability_status(table_id):

    cur.execute(tables)
    table_data = cur.fetchall()
    for table in table_data:
        if table[0] == table_id and table[4] == False:
            return True

    return False


def get_order_details():

    cur.execute(orders)
    data = cur.fetchall()
    return data

def post_online_order_details(req):

    req = req.json
    menu_id = req.get("menu_id")
    res_id = req.get("restaurant_id")
    table_id = req.get("table_id")
    user_id = req.get("user_id")

    data = (menu_id, user_id, res_id, table_id)

    flag = check_table_availability_status(table_id)

    try:
        if flag == True:
            data = cur.execute(order_insert, data)
            response_data = process_payment(req)
            return response_data
        else:
            return "The selected table already reserved. Please select the other table please"

    except:
        return "The order hasn't placed. Please verify the data"

def process_payment(req):

    id = req.get('menu_id')
    query = menu_id.format(id)
    cur.execute(query)
    data = cur.fetchone()
    return "total amount of the order is {}".format(data[4]) 






