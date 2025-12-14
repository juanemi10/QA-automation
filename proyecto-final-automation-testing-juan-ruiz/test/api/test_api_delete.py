import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/1")

    assert response.status_code == 200
