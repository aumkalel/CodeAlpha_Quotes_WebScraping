import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []
tags_list = []

all_quotes = soup.find_all("div", class_="quote")

for quote in all_quotes:

    text = quote.find("span", class_="text").text

    author = quote.find("small", class_="author").text

    tags = [tag.text for tag in quote.find_all("a", class_="tag")]

    quotes.append(text)
    authors.append(author)
    tags_list.append(", ".join(tags))

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags_list
})

df.to_csv("quotes_dataset.csv", index=False)

print("Dataset Created Successfully!")