import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from requests import get
only_a = SoupStrainer("a")

#Category list:

category_url = requests.get("https://bdsmstreak.com/categories")
category = BeautifulSoup(category_url.text,'html.parser')

a_category = category.select('a[href*="category"]')

for link in a_category:
    print("https://bdsmstreak.com" + link.get("href"))


#Page range get:

page_count_get = requests.get("https://bdsmstreak.com/category/gangbang-bdsm")
page_count = BeautifulSoup(page_count_get.text, 'html.parser')
count = page_count.select("ul.pagination li")
lenght = len(count)
print(lenght)
print(count[lenght - 2].get_text())