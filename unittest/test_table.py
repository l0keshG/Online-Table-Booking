import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_get_table_details():

    response = requests.get(url+ '/tables')
    assert response.status_code == 200