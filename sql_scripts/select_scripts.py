restaurant = 'select * from booking.restaurant'

menus = 'select * from booking.menus'

user_details = 'select * from booking.user_details'

tables = 'select * from booking.tables'

#select menu with restaurant and tables

custom_menu = 'select * from booking.menus where restaurant_id = r_id and tables_id= t_id'

