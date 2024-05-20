import json
import requests

from bs4 import BeautifulSoup

from init import ua
from config import START_URL, END_URL, START_URL_FOR_PAGES, END_URL_FOR_PAGES


def collect(bs: BeautifulSoup) -> list[dict]:
    vacancies = []

    items = bs.find_all("div", class_="vacancy-card--H8LvOiOGPll0jZvYpxIF font-inter")

    for item in items:
        label = item.find(
            "span",
            class_="vacancy-name--SYbxrgpHgHedVTkgI_cA serp-item__title-link serp-item__title-link_redesign",
        ).get_text()

        link = item.find("a", class_="bloko-link").get("href")

        try:
            salary = item.find(
                "span",
                class_="compensation-text--cCPBXayRjn5GuLFWhGTJ fake-magritte-primary-text--qmdoVdtVX3UWtBb3Q7Qj separate-line-on-xs--pwAEUI79GJbGDu97czVC",
            ).get_text()
        except:
            salary = "-"

        try:
            experience = item.find(
                "span",
                class_="label--rWRLMsbliNlu_OMkM_D3 label_light-gray--naceJW1Byb6XTGCkZtUM",
            ).get_text()
        except:
            experience = "-"

        vacancies.append(
            {"label": label, "link": link, "salary": salary, "experience": experience}
        )
    return vacancies


def get_vacancies(id: int):
    print("Идет сбор данных, подождите")
    try:
        url = START_URL + str(id) + END_URL
        responce = requests.get(url=url, headers={"user-agent": ua.random})

        bs = BeautifulSoup(responce.text, "lxml")

        items_count = int(
            bs.find("h1", class_="bloko-header-section-3").get_text().split()[1]
        )
        vacancies = {"content": []}

        vacancies["content"].extend(collect(bs))

        for i in range(1, items_count // 20 + 1):
            url = START_URL_FOR_PAGES + str(id) + END_URL_FOR_PAGES + str(i)

            responce = requests.get(url=url, headers={"user-agent": ua.random})
            vacancies["content"].extend(collect(BeautifulSoup(responce.text, "lxml")))

        with open(f"result_by_vacancy_{id}.json", "w", encoding="utf-8") as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

        return f"Завершено. Всего вакансий: {len(vacancies['content'])}"
    except:
        return "Ошибка"
