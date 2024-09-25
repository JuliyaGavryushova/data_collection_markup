"""
Сценарий Foursquare.
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию
(например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.
"""
import requests
import json

client_id = "MR32BSBPGFI2Y4GFEXNRFBLERYYXVN2V4JNT0SX4HNYCAING"
client_secret = "MSXFQ4L5STIYIP4XDMF0N5AKRIB1JVQHBZUMBBXR003MXJPZ"

city = input("Введите название города: ")
place = input("Введите заведение: ")

url = "https://api.foursquare.com/v3/places/search"

params = {"client_id": client_id,
          "client_secret": client_secret,
          "near": city,
          "query": place}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3BEgtuhn9a5pFlSAmSQWhEDSXcj/kqiPWS/AEUWTl8uA="
}
# headers = {
#     "Accept": "*/*"
# }

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Адрес:", venue["location"]["address"])
        print("Почта:", venue["location"]["postcode"])
        print("Регион:", venue["location"]["region"])
        print("Город:", venue["location"]["locality"])
        print("Аббревиатура:", venue["location"]["country"])
        print("Часовой пояс:", venue["timezone"])
        print("Ссылка:", venue["link"])
        print("Идентификатор:", venue["fsq_id"])
        print("\n")
else:
    print("Запрос завершился ошибкой")
    print(response.status_code)

