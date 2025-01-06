import pytest
import requests
import responses

from backend.app.logic import request_sender
from backend.app.services.json_loader import load_json_data
import json



# Тестовые данные
TEST_URL = "https://example.com/test"

# Загрузка headers и data из файлов
HEADERS = load_json_data()

with open("data.json", "r") as f:
    DATA = json.load(f)

@responses.activate
def test_send_request_get():
    responses.add(responses.GET, TEST_URL, json={"message": "success"}, status=200)

    response = request_sender(TEST_URL, method='GET', headers=HEADERS)

    assert response is not None
    assert response.status_code == 200
    assert response.json() == {"message": "success"}

@responses.activate
def test_send_request_post():
    responses.add(responses.POST, TEST_URL, json={"message": "created"}, status=201)

    response = request_sender(TEST_URL, method='POST', data=DATA, headers=HEADERS)

    assert response is not None
    assert response.status_code == 201
    assert response.json() == {"message": "created"}

@responses.activate
def test_send_request_put():
    responses.add(responses.PUT, TEST_URL, json={"message": "updated"}, status=200)

    response = request_sender(TEST_URL, method='PUT', data=DATA, headers=HEADERS)

    assert response is not None
    assert response.status_code == 200
    assert response.json() == {"message": "updated"}

@responses.activate
def test_send_request_delete():
    responses.add(responses.DELETE, TEST_URL, status=204)

    response = request_sender(TEST_URL, method='DELETE', headers=HEADERS)

    assert response is not None
    assert response.status_code == 204

@responses.activate
def test_send_request_invalid_method():
    with pytest.raises(ValueError, match="Unsupported HTTP method: INVALID"):
        request_sender(TEST_URL, method='INVALID')

@responses.activate
def test_send_request_error():
    responses.add(responses.GET, TEST_URL, body=requests.RequestException("Connection error"))

    response = request_sender(TEST_URL, method='GET')

    assert response is None
