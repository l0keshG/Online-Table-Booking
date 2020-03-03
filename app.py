from flask import Flask, jsonify
from controllers.restaurant import get_restaurants
from controllers.menu import get_menu_data
from controllers.table import get_table_data
from controllers.order import post_order_details

app = Flask(__name__)

@app.route('/restaurants', methods=['GET'])
def get_restaurant_details():
    data = get_restaurants()
    return jsonify(data)

@app.route('/menu', methods=['GET'])
def get_menu_details():
    data = get_menu_data()
    return jsonify(data)

@app.route('/tables', methods=['GET'])
def get_table_details():
    data = get_table_data()
    return jsonify(data)

@app.route('/health', methods=['GET'])
def health():
    return jsonify("this is good!!!")

@app.route('/order_details', methods=['POST'])
def order_details(request):
    data = post_order_details(request)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)