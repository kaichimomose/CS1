import requests
from bs4 import BeautifulSoup


quote_page = "https://www.makeschool.com/product-college/students"

page = requests.get(quote_page)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
