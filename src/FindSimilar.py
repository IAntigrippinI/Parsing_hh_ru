from init import avilable_roles
from config import LIMIT_SPECIALIZATION_OUTPUT


def find_similar(inp: str) -> str:
    result = []
    for role in avilable_roles:

        if inp in role["name"].lower():

            result.append(f"[{role['id']}] {role['name']}")

            if len(result) >= LIMIT_SPECIALIZATION_OUTPUT:
                break
    if len(result) == 0:
        return "Совпадений не найдено"

    return "\n".join(result)
