import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_menu_details():

    response = requests.get(url+ '/menu')
    assert response.status_code == 200