import requests
from bs4 import BeautifulSoup
import lxml
# from proxy_auth import proxies
import json

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
url = "https://www.skiddle.com/api/v1/events/search/?limit=8&offset=44&radius=5&minDate=2022-12-03T00%3A00%3A00&hidecancelled=1&order=trending&showVirtualEvents=0&artistmeta=1&artistmetalimit=3&aggs=genreids%2Ceventcode&pub_key=42f25&platform=web&collapse=uniquelistingidentifier"
# # print(url)
# for i in range(0, 8, 8):
#     # for i in range(0, 796, 8):
#     req = requests.get(url=url,headers=headers)
#     json_data = json.loads(req.text)
#     html_response = json_data["html"]
#
#     with open(f"index_{i}.html", 'w') as file:
#         file.write(html_response)

req = requests.get(url, headers=headers)
src = req.text

with open('index.html', 'w', encoding='utf-8-sig') as file:
    file.write(src)

# soup = BeautifulSoup(src, 'lxml')

