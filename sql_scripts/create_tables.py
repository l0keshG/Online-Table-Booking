restaurants = 'CREATE TABLE booking.restaurant
(
	id serial NOT NULL CONSTRAINT restaurant_pkey PRIMARY KEY,
	name varchar(100) NOT NULL,
	restaurant_type varchar(100),
	location varchar(256),
	city varchar(100),
	pincode varchar(100)
);'

menus = 'CREATE TABLE booking.menus
(
	id serial NOT NULL CONSTRAINT menu_pkey PRIMARY KEY,
	restaurant_id integer references booking.restaurant(id),
	tables_id integer references booking.tables(id),
	menu_name varchar(100) NOT NULL,
	menu_price integer
);'

tables = 'CREATE TABLE booking.tables
(
	id serial NOT NULL CONSTRAINT table_pkey PRIMARY KEY,
	restaurant_id integer references booking.restaurant(id),
	table_name varchar(100) NOT NULL,
	table_number varchar(100),
	reserved boolean
);'

user_details = 'CREATE TABLE booking.user_details (
  id serial not null constraint user_pkey primary key,
  user_name varchar(256) not null constraint user_ukey unique key,
  first_name varchar(256),
  last_name varchar(256),
  email varchar(256),
  created_at timestamp with time zone default (now() at time zone 'utc')
);'