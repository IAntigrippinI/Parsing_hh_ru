import os.path

import requests
import asyncio

from bs4 import BeautifulSoup
from multiprocessing import Pool

from init import ua
from config import SPECIALIZATIONS_FILE_PATH


def check_exist_file() -> bool:
    if os.path.exists(SPECIALIZATIONS_FILE_PATH):
        return True
    else:
        return False


def add_specialization_label_in_file(url):

    ind_start_role = url.find("professional_role=")
    ind_end_role = url.find("&", ind_start_role)
    role = url[ind_start_role + 18 : ind_end_role]

    responce = requests.get(url, headers={"user-agent": ua.random})

    bs = BeautifulSoup(responce.text, "lxml")

    menu = bs.find_all("div", class_="nova-control--GtG8Kpo7kAMGijnRbxtY")

    target_pos = -1
    for i in range(len(menu)):
        try:
            if "Специализации" in menu[i].find("legend"):
                target_pos = i
        except:
            pass

    if target_pos != -1:
        with open(SPECIALIZATIONS_FILE_PATH, "a", encoding="utf-8") as file:
            try:
                data = menu[target_pos].find("span", class_="bloko-checkbox__text")

                file.write(role + " : " + data.find("span").text + "\n")
            except Exception as e:
                print(e)


def get_specializations():

    lst = []

    for role in range(1, 175):
        url = f"https://vladivostok.hh.ru/search/vacancy?L_save_area=true&area=22&items_on_page=50&hhtmFrom=vacancy_search_filter&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&part_time=from_four_to_six_hours_in_a_day&part_time=employment_part&professional_role={role}&text="
        lst.append(url)

    with Pool() as pool:
        pool.map(add_specialization_label_in_file, lst)
