from flask import Flask, jsonify, request
from controllers.restaurant import get_restaurants
from controllers.menu import get_menu_data, custom_menu_details
from controllers.table import get_table_data
from controllers.order import post_order_details, get_order_details
from controllers.user_details import get_user_data

app = Flask(__name__)

@app.route('/restaurants', methods=['GET'])
def get_restaurant_details():
    data = get_restaurants()
    return jsonify(data), 200

@app.route('/menu', methods=['GET'])
def get_menu_details():
    data = get_menu_data()
    return jsonify(data), 200

@app.route('/user_details', methods=['GET'])
def get_user_details():
    data = get_user_data()
    return jsonify(data), 200

@app.route('/tables', methods=['GET'])
def get_table_details():
    data = get_table_data()
    return jsonify(data), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify("this is good!!!"), 200

@app.route('/order_details', methods=['POST', 'GET'])
def order_details():
    if request.method == 'POST':

        data = post_order_details(request)
        return jsonify(data), 201
    elif request.method == 'GET':
        data = get_order_details()
        return jsonify(data), 200

@app.route('/custom_menu', methods=['GET'])
def get_custom_menu_details():
    data = custom_menu_details(request)
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=True)