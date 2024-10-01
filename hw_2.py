from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint
import requests
import json

ua = UserAgent()

url = "https://books.toscrape.com/"
headers = {"User-Agent": ua.random}
params = {"page": 1}

# response = requests.get(url + "", headers=headers, params=params)
#
# soup = BeautifulSoup(response.text, "html.parser")
#
# books = soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
# print(len(books))

all_books = []

while True:
    response = requests.get(url + "", headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    if not books:
        break

    for book in books:
        book_info = {}

        add_info = book.find("article", {"class": "product_pod"})

        name_info = add_info.find("h3")
        book_info["name"] = name_info.getText()

        price_info = add_info.find("div", {"class": "product_price"}).find("p", {"class": "price_color"})
        book_info["price"] = float(price_info.text[2:])

        book_info["stock"] = soup.find("p", {"class": "instock availability"}).text.split()[:2]

        all_books.append(book_info)

    params["page"] += 1

# pprint(all_books)
# print(len(all_books))

with open('books_data.json', 'w') as f:
    json.dump(all_books, f, indent=2)