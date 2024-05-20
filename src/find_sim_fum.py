from init import specializations
from config import LIMIT_SPECIALIZATION_OUTPUT


def find_similar(name: str) -> str:
    count = 0
    print(f"in fun {len(specializations['content'])}")

    similar = ""
    for role in specializations["content"]:
        if count == LIMIT_SPECIALIZATION_OUTPUT:
            return similar
        if name in role["label"].lower():
            similar += f"[{role['id']}] {role['label']}\n"
            count += 1
    return similar
