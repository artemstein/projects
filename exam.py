import sqlite3
import requests
from bs4 import BeautifulSoup
from bs4 import Tag
#
connection = sqlite3.connect("exam_DB.sl3", 5)
cur = connection.cursor()
# cur.execute("DELETE FROM exam_table")
cur.execute("SELECT name FROM exam_table;")
res = cur.fetchall()
#
# links = ["https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B2%D1%96%D1%82%D1%80%D1%8F%D0%BD%D1%96_%D1%81%D0%B8%D0%BB%D0%B8_%D0%97%D0%B1%D1%80%D0%BE%D0%B9%D0%BD%D0%B8%D1%85_%D1%81%D0%B8%D0%BB_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8",
#         "https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B2%D1%96%D1%82%D1%80%D1%8F%D0%BD%D1%96_%D1%81%D0%B8%D0%BB%D0%B8_%D0%A1%D0%A8%D0%90",
#         "https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B2%D1%96%D1%82%D1%80%D1%8F%D0%BD%D1%96_%D1%81%D0%B8%D0%BB%D0%B8_%D0%9D%D1%96%D0%BC%D0%B5%D1%87%D1%87%D0%B8%D0%BD%D0%B8"]
# for link in links:
#     cur.execute("INSERT INTO exam_table (name) VALUES (?)", (link,))


# if res1.status_code == 200:
#     soup1 = BeautifulSoup(text1, features="html.parser")
#     soup1_list = ""
#     for item1 in soup1.find_all("div", {"id": "bodyContent"}):
#         soup1_list += item1.text
#         matches1 = soup1.find(string=lambda text: res1 in text)
#         print(matches1)


search_term = input("Введіть інформацію для пошуку: ")

for link in res:
    page = requests.get(link[0])
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.get_text()
    if search_term in results:
        print("Знайдено на сторінці", link[0])

connection.commit()
connection.close()
