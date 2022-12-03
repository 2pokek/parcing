import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#     "accept": "*/*",
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
# req = requests.get(url,headers=headers)
# src = req.text
# print(src)

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
all_category_dict = {}
for item in all_products_hrefs:
    # print(item)
    item_text = item.text
    item_href = "https://health-diet.ru" + item.get("href")
    # print(f"{item_text}:{item_href}")
    all_category_dict[item_text] = item_href

with open("all_category_dict.json", 'w') as file:
    json.dump(all_category_dict, file, indent=4, ensure_ascii=False)
