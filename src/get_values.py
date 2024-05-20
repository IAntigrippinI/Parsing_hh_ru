import requests

from config import URL_FOR_GET_PROFESSIONAL_ROLES


def get_roles() -> list[dict]:
    responce = requests.get(URL_FOR_GET_PROFESSIONAL_ROLES).json()
    cat = responce["categories"]

    roles = []

    for category in cat:
        data = category["roles"]

        add = [{"id": data[i]["id"], "name": data[i]["name"]} for i in range(len(data))]

        roles.extend(add)

    return roles
