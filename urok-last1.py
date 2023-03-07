import requests
from bs4 import BeautifulSoup


response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")


if response.status_code == 200:
    my_dict = {}
    soup = BeautifulSoup(response.text, features="html.parser")
    name_list = soup.find_all("td", {"class": "value-name"})
    value_list = soup.find_all("td", {"data-label": "Офіційний курс"})
    for key, value in zip(name_list, value_list):
        my_dict[key.text.replace("\n", "").replace(" ", "")] = value.text
    for key, value in my_dict.items():
        print(f"Назва валюти - {key}\n Офіційний курс - {value}\n")
    while True:
        try:
            amount = float(input("Введіть кількість гривень: "))
            break
        except ValueError:
            print("Будь ласка, введіть числове значення.")
    currency = input("Введіть назву валюти: ").strip()
    if currency in my_dict:
        exchange_rate = float(my_dict[currency].replace(",", "."))
        conversion = amount / exchange_rate
        print(f"{amount} грн = {conversion} {currency}")
    else:
        print("Вказана валюта не знайдена.")
else:
    print("Помилка при відкритті веб-сторінки.")
