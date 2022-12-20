import datetime
import json
import requests

def get_data():
    start_time = datetime.datetime.now()

    url = "https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1=1"
    r = requests.get(url=url, headers=headers)

    with open("index.html", "w") as file:
        file.write(r.text)

def main():
    get_data()


if __name__ == '__main__':
    main()