from os import writev
import requests
from bs4 import BeautifulSoup
import json
import csv
import re

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# url = "https://svetofor.info/categories/"

# req = requests.get(url, headers=headers)
# src = req.text

# with open("index.html", "w") as file:
#     file.write(src)

# with open("lesson2/index.html") as file:
#     src = file.read()

# soup = BeautifulSoup(src, 'lxml')

# all_products_links_li = soup.find_all(class_="sub_sub_cat")

# all_cat_dict = {}


# for link in all_products_links_li:
#     link_a = link.find('a')
#     link_a_text = link_a.text
#     link_a_href = link_a.get("href")

#     all_cat_dict[link_a_text] = link_a_href

# with open("lesson2/all_cat_dict.json", "w") as file:
#     json.dump(all_cat_dict, file, indent=4, ensure_ascii=False)

with open("lesson2/all_cat_dict.json") as file:
    all_cat = json.load(file)

count = 1
for cat_name, cat_href in all_cat.items():
    rep = [',', ' ', '-', "'", '_']

    if count == 2:
        for item in rep:
            if item in cat_name:
                cat_name = cat_name.replace(item, '_')
        
        req = requests.get(url=cat_href, headers=headers)
        src = req.text

        with open(f"lesson2/data/{count}_{cat_name}.html", 'w') as file:
            file.write(src)
        
        with open(f"lesson2/data/{count}_{cat_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        alert_block = soup.find(class_="ty-no-items")
        if alert_block is not None:
            continue

        with  open(f"lesson2/data/csv/{count}_{cat_name}.csv", 'w', encoding="utf-8") as file:
            # writing titles
            writer = csv.writer(file)
            writer.writerow((
                'Наименование',
                'Старая цена'
                'Цена',
                'Код товара'
            ))

        #writing data
        products_data = soup.find(class_="grid-list").find_all(class_="ty-column4")
        
        for data in products_data:
            data_item = data.find(class_="ty-grid-list__item")
            data_form = data_item.find("form")
            data_title = data_form.find(class_="ty-grid-list__item-name").text
            data_price_container = data_form.find(class_="ty-grid-list__price")
            data_old_price = data_price_container.find(id=re.compile("old_price")).text.strip()
            data_price = data_price_container.find(class_="ty-price").text.strip()
            data_code = data_form.find(class_="sv_prod_code").text

            with  open(f"lesson2/data/csv/{count}_{cat_name}.csv", 'a', encoding="utf-8") as file:
                # writing data
                writer = csv.writer(file)
                writer.writerow((
                    data_title,
                    data_old_price,
                    data_price,
                    data_code
                ))

        count += 1