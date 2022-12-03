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

with open('all_category_dict.json', encoding='utf-8-sig') as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories) - 1)
count = 0
print(f'{iteration_count} - Всего итераций')

for category_name, category_href in all_categories.items():

    rep = [',', ' ', '-', "'"]
    for item in rep:
        if item in category_name:
             category_name = category_name.replace(item, '_')
        # print(category_name)

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{category_name}_{count}.html",'w', encoding='utf-8-sig') as file:
        file.write(src)
    with open(f"data/{category_name}_{count}.html", encoding='utf-8-sig') as file:
        src=file.read()

    soup = BeautifulSoup(src,'lxml')

    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue
    table_head = soup.find(class_='mzr-block uk-margin-top').find('tr').find_all('th')
    # print(table_head)
    product = table_head[0].text
    calories = table_head[1].text
    protiens = table_head[2].text
    fats = table_head[3].text
    carbs = table_head[4].text

    with open(f"data/{category_name}_{count}.csv",'w',encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                protiens,
                fats,
                carbs,

            )
        )

    product_data=soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    product_info = []
    for item in product_data:
        product_tds = item.find_all('td')

        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        protiens = product_tds[2].text
        fats = product_tds[3].text
        carbs = product_tds[4].text

        product_info.append({
            "Title":title,
            "Calories":calories,
            "Protiens":protiens,
            "Fats":fats,
            "Carbs":carbs,
        })

        with open(f"data/{category_name}_{count}.csv", 'a', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    protiens,
                    fats,
                    carbs,

                )
            )
    with open(f"data/{category_name}_{count}.json",'a',encoding="utf-8-sig") as file:
        json.dump(product_info,file,indent=4,ensure_ascii=False)
    count += 1
    print(f"# Iteration {count},{category_name} recorded...")
    iteration_count = iteration_count - 1
    if iteration_count == 0:
        print('Work is done!')
    print(f'Iterations left: {iteration_count}')
    sleep(random.randrange(1,3))


