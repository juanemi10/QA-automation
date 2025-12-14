import json
import os


def load_json(file_name):
    """
    Carga un archivo JSON desde la carpeta data
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_valid_users():
    data = load_json("users.json")
    return data["valid_users"]


def get_invalid_users():
    data = load_json("users.json")
    return data["invalid_users"]
