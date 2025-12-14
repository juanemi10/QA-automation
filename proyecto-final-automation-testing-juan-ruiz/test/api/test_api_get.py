import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert "id" in body[0]
