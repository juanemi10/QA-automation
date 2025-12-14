import json
import os


def load_users(user_type):
    """
    Carga usuarios desde data/users.json
    user_type puede ser:
    - valid
    - invalid
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", "users.json")

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if user_type == "valid":
        return data["valid_users"]

    if user_type == "invalid":
        return data["invalid_users"]

    raise ValueError("Tipo de usuario no soportado")
