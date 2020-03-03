restaurant = 'select * from booking.restaurants'

menus = 'select * from booking.menus'

user_details = 'select * from booking.user_details'

tables = 'select * from booking.tables'

#select menu with restaurant and tables

custom_menu = f'select * from booking.menus where restaurant_id = {a} and tables_id= {b}'.format(a,b)

