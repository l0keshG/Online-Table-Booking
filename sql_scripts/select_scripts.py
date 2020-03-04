restaurant = 'select * from booking.restaurant'

menus = 'select * from booking.menus'

user_details = 'select * from booking.user_details'

tables = 'select * from booking.tables'

orders = 'select * from booking.order_details'

#select menu with restaurant and tables

custom_menu = 'select * from booking.menus where restaurant_id = {} and tables_id= {}'

#select by id

menu_id = 'select * from booking.menus where id={}'

user_detail_id = 'select * from booking.user_details where id = {}'

table_id = 'select * from booking.tables where id = {}'

order_id = 'select * from booking.order_details where id = {}'