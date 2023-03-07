import sqlite3
import requests
from bs4 import BeautifulSoup

response = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D1%88%D0%B8%D0%BD%D1%91%D0%B2/2023-03-06")

connection = sqlite3.connect('database_DB.sl3', 5)
cur = connection.cursor()


if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("tr", {"class": "temperature"})
    temperature = soup_list[0].find("td", {"class": "p5"}).get_text()
    soup_list_time = soup.find_all("tr", {"class": "gray time"})
    data_time = soup_list_time[0].find("td", {"class": "p5"}).get_text()
    cur.execute("INSERT INTO first_table (temperature, data) VALUES (?,?)", (temperature,data_time))
    connection.commit()
    connection.close()
