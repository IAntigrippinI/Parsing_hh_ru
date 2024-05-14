import json
import requests
import asyncio

from bs4 import BeautifulSoup
from pathlib import Path

from init import ua
from functions_for_Specialization import get_specializations, check_exist_file


def collect_info():
    pass


def main():
    if check_exist_file():
        collect_info()
    else:
        get_specializations()
        collect_info()


if __name__ == "__main__":

    import os

    if not os.path.exists("src/data"):
        os.makedirs("src/data")
    main()
