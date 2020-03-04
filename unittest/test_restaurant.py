import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_restaurant_details():

    response = requests.get(url+ '/restaurants')
    assert response.status_code == 200