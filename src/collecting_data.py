import json
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from config import START_URL, END_URL


def collect_data(id: int):

    ua = UserAgent()
    url = START_URL + str(id) + END_URL

    responce = requests.get(url=url, headers={"user-agent": ua.random})
