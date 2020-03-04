import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_health():

    response = requests.get(url+ '/health')
    assert response.status_code == 200