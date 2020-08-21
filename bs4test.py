import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from requests import get
only_a = SoupStrainer("a")


category_url = requests.get("https://bdsmstreak.com/categories")
category = BeautifulSoup(category_url.text,'html.parser')

a_category = category.select('a[href*="category"]')

for link in a_category:
    print("https://bdsmstreak.com" + link.get("href"))
