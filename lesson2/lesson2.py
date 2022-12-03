import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open('index.html', encoding='utf-8-sig') as file:
#     # file.write(src)
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
#
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
# all_category_dict = {}
# for item in all_products_hrefs:
#     # print(item)
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#     # print(f"{item_text}:{item_href}")
#     all_category_dict[item_text] = item_href
#
# with open("all_category_dict.json", 'w', encoding='utf-8-sig') as file:
#     json.dump(all_category_dict, file, indent=4, ensure_ascii=False)

with open('all_category_dict.json',encoding='utf-8-sig') as file:
    all_categories = json.load(file)

    count = 0
    for category_name, category_href in all_categories.items():
        if count == 0:
            rep = [',', ' ', '-', "'"]
            for item in rep:
                if item in category_name:
                    category_name = category_name.replace(item, '_')
                # print(category_name)

            req = requests.get(url=category_href, headers=headers)
            src = req.text

            with open(f"data/{category_name}_{count}.html", 'w',encoding='utf-8-sig') as file:
                file.write(src)

            count += 1
