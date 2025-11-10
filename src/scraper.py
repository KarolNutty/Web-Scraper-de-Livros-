import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titulos = [book.h3.a["title"] for book in soup.find_all("article", class_="product_pod")]
precos = [book.find("p", class_="price_color").text for book in soup.find_all("article", class_="product_pod")]

df = pd.DataFrame({"titulo": titulos, "preco": precos})
df.to_csv("livros.csv", index=False)

print("Scraping completo! Dados salvos em livros.csv")
