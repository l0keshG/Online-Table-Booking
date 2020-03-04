import pytest
import requests

url = 'http://127.0.0.1:5000'

order_payload = {
   "menu_id": 1,
   "restaurant_id": 101,
   "table_id": 1004,
   "user_id": 1
}

@pytest.mark.xfail
def test_post_order_details():

    response = requests.post(url+ '/order_details', order_payload)
    assert response.status_code == 201

def test_get_order_details():

    response = requests.get(url+ '/order_details')
    assert response.status_code == 200
