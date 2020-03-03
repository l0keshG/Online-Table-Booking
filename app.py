from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/restaurants', methods=['GET'])
def get_restaurant_details():
    return jsonify("response")



if __name__ == '__main__':
    app.run(debug=True)