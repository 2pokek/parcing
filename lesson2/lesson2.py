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

with open('index.html','w') as file:
    file.write(src)