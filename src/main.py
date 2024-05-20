import json

from req import get_vacancies
from FindSimilar import find_similar

from init import avilable_roles
from config import INFO_TEXT


def main():
    print(INFO_TEXT)
    while True:
        inp = input("Ввод: ")
        if inp == "q":
            break
        elif inp.replace(" ", "").isdigit():
            print(get_vacancies(int(inp.replace(" ", ""))))
        else:
            print(find_similar(inp.lower()))


if __name__ == "__main__":
    main()
