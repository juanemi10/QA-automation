import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_user():
    payload = {
        "name": "Juan",
        "username": "juanruiz",
        "email": "juan@test.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=payload
    )

    assert response.status_code == 201

    body = response.json()
    assert body["name"] == "Juan"
