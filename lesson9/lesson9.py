import json
import time
import requests
from bs4 import BeautifulSoup
import datetime
import csv


start_time = time.time()


def get_data():
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"labirint_{cur_time}.csv", "w") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Название книги",
                "Автор",
                "Издательство",
                "Цена со скидкой",
                "Цена без скидки",
                "Процент скидки",
                "Наличие на складе"
            )
        )

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    url = "https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=table"

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)