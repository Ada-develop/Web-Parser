import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import pandas as pd
from requests import get
from time import sleep
from random import randint
only_a = SoupStrainer("a")

#Category list:

category_url = requests.get("https://bdsmstreak.com/categories")
category = BeautifulSoup(category_url.text,'html.parser')

a_category = category.select('a[href*="category"]')

for link in a_category:
    print("https://bdsmstreak.com" + link.get("href"))


categories = []
page_range = []

##################################################################
#Category URL get:

category_url = requests.get("https://bdsmstreak.com/categories")
category = BeautifulSoup(category_url.text,'html.parser')

a_category = category.select('a[href*="category"]')

for link in a_category:
    categories.append("https://bdsmstreak.com" + link.get("href"))
###################################################################
#Range of pages:

for page in categories:
    page_count_get = requests.get(page)
    page_count = BeautifulSoup(page_count_get.text, 'html.parser')
    count = page_count.select("ul.pagination li")
    lenght = len(count)
    page_range.append(count[lenght - 2].get_text())
    sleep(randint(2,10))

category_count = pd.DataFrame({
    'catogory' : categories,
    'page_range' : page_range,
})

category_count.to_csv("./category_and_range.csv")


#Page range get:
for cnt in count:
   page_range.append(cnt)

page_count_get = requests.get("https://bdsmstreak.com/category/gangbang-bdsm")
page_count = BeautifulSoup(page_count_get.text, 'html.parser')
count = page_count.select("ul.pagination li")
lenght = len(count)
print(lenght)
print(count[lenght - 2].get_text())