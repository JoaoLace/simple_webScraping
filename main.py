import requests
from bs4 import BeautifulSoup
import csv


def saveToCsv (book_title, book_price):
    with open("books.csv", mode="+a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([book_title, book_price])

URL = "http://books.toscrape.com/"

try:
    page = requests.get(URL)
    page.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching the page {e}")

soup = BeautifulSoup(page.content, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    book_name = book.h3.a
    book_price = book.find("p", class_="price_color")

    print(f"Book name: {book_name.get_text()}")
    print(f"Book price: {book_price.text}")

    saveToCsv(book_name.get_text(), book_price.text)

    print("-"*40)
