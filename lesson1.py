#pip install beautifulsoup4 lxml

from bs4 import BeautifulSoup
import re

with open("blank/index.html") as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, 'lxml')

# title = soup.title

# print(title)
# print(title.text)
# print(title.string)

# .find() .find_all()

# page_h3 = soup.find("h3")
# page_all_h3 = soup.find_all("h3")

# for item in page_all_h3:
#     print(item.text)

# user_name = soup.find("span", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find(class_="user__name").find("div").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name"}).find("span").text
# print(user_name)


# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# for item in find_all_spans_in_user_info:
#     print(item.text.strip())

# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[0].text)

# social_network = soup.find("footer").find_all("a")
# print(social_network)

# all_a = soup.find_all("a")
# # print(all_a)

# for i in all_a:
#     i_text = i.text
#     i_url = i.get("href")
#     # print(i_url)
#     print(f"{i_text.strip()}: {i_url}")

# .find_parrent() .find_parrents()

# post_div = soup.find(class_="card-text").find_parent()
# print(post_div)

# post_div = soup.find(class_="card-text").find_parent("div", "card-body")
# print(post_div)

# post_divs = soup.find(class_="card-text").find_parents()
# print(post_divs)

# .next_element .previous_element

# next_el = soup.find(class_="card-text").next_element.next_element.next_element
# print(next_el)

# next_el = soup.find(class_="card-text").find_next().text.strip()
# print(next_el)

# links = soup.find(class_="some_link").find_all("a")
# print(links)

# for link in links:
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]
#     link_data_attr = link.get("data-attr")
#     link_data_attr1 = link["data-attr"]

#     print(link_data_attr1)
#     print(link_href_attr1)

# find_a_text = soup.find("a", text="Link")
# print(find_a_text)

# find_a_text = soup.find("a", text="Link 1")
# print(find_a_text)

find_a_text = soup.find("a", text = re.compile("Link"))
print(find_a_text)

find_all_a = soup.find_all("a", text=re.compile("[Ll]ink"))
print(find_all_a)