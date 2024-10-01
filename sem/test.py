from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pprint import pprint
import requests
import pandas as pd

ua = UserAgent()

# url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"
url = "https://www.boxofficemojo.com"
headers = {"User-Agent": ua.random}
params = {"ref_": "bo_nb_hm_tab"}

response = requests.get(url + "/intl", params=params, headers=headers)

# print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
# test_link = soup.find("a", {"class": "a-link-normal"})
#
# print(test_link)

rows = soup.findAll("tr")

films = []

for row in rows[2:]:
    film = {}
    # area_info = row.find("td", {"class": "mojo-field-type-area_id"}).find("a")
    area_info = row.find("td", {"class": "mojo-field-type-area_id"}).findChildren()[0]
    film["area"] = [area_info.getText(), url + area_info.get("href")]

    weekend_info = row.find("td", {"class": "mojo-field-type-date_interval"}).findChildren()[0]
    film["weekend"] = [weekend_info.getText(), url + weekend_info.get("href")]

    film["releases"] = int(row.find("td", {"class": "mojo-field-type-positive_integer"}).getText())

    first_releases_info = row.find("td", {"class": "mojo-field-type-release"}).findChildren()[0]
    film["first_releases"] = [first_releases_info.getText(), url + first_releases_info.get("href")]

    try:
        distributor_info = row.find("td", {"class": "mojo-field-type-studio"}).findChildren()[0]
        film["distributor"] = [distributor_info.getText(), url + distributor_info.get("href")]
    except:
        film["distributor"] = None

    # film["weekend_gross"] = int(row.find("td", {"class": "mojo-field-type-money"}).getText())

    films.append(film)

pprint(films)