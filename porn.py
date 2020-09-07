#import tools:
# sleep() function from time module will control loop's rate of flooding
# randint() from random modul, will vary amount of waiting time between requests - within specified interval

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint

#Steps of multiple-page parsing:
#Request the URL for every page on site
#Iterate through each page using a for loop, and scrape each <a href=""> of movie div
#Control loop's rate to avoid flooding the server with requests
#Extract,clean and download final data
#Basic data-quality practice

#Intialize storage:
#
# category_url = requests.get("https://bdsmstreak.com/categories")
# category = BeautifulSoup(category_url.text,'html.parser')
#
# a_category = category.select('a[href*="category"]')
#
#
# for link in a_category:
#     categories.append("https://bdsmstreak.com" + link.get("href"))

title = []
duration = []
link = []
category_movie = []
categories = []
page_range = []

#Category URL get:

category_url = requests.get("https://bdsmstreak.com/categories")
category = BeautifulSoup(category_url.text,'html.parser')
a_category = category.select('a[href*="category"]')

for links in a_category:
    categories.append("https://bdsmstreak.com" + links.get("href"))

#Page range get:

getting_range = 1

for page in categories:
    page_count_get = requests.get(page)
    page_count = BeautifulSoup(page_count_get.text, 'html.parser')
    count = page_count.select("ul.pagination li")
    lenght = len(count)
    page_range.append(count[lenght - 2].get_text())
    name_category = page.replace("https://bdsmstreak.com/category/","")
    print("Getting category : " + str(name_category) +" | Range is : "+ str(getting_range) + " / 44")
    getting_range = getting_range + 1
    sleep(randint(2,10))

#Creating dictionary:
category_page_dict = dict(zip(categories,page_range))

###################################################################
#pages = np.arange(1,count_page,1)
#Looping through each page
#Request(URL) + 'html_soup' + 'porn_link'
#Counting pages while looping:
#rng_pg cat
for cat,rng_pg in category_page_dict.items():

    page_number = 1

    rng = np.arange(1,int(rng_pg),1)

    for range in rng:
        print("Requesting " + str(cat) + "?page=" + str(range))
        page = requests.get(str(cat) + "?page=" + str(range))
        soup = BeautifulSoup(page.text, 'html.parser')
        porn = soup.findAll('a', class_='vidlink')
        durations = soup.findAll("div", class_="duration")
        titles = soup.findAll("div", class_="videotitle")

        for links in porn:
            print("Collect link")
            url = "https://bdsmstreak.com" + links.get("href")
            link.append(url)

        for tit in titles:
            print("Collect title")
            name = tit.get_text()
            title.append(name)

        for dur in durations:
            print("Collect duration")
            dura = dur.get_text()
            duration.append(dura)
            category_movie.append(str(cat).replace("https://bdsmstreak.com/category/","").title())
            print("Title : " + str(tit.get_text()) +  ", Duration : " + str(dur.get_text()) + ", Category : " + str(cat).replace("https://bdsmstreak.com/category/","").title())

        name_category = cat.replace("https://bdsmstreak.com/category/","")
        print("Current category : "+ str(name_category).title() + " | Current page: " + str(page_number) + " / " + str(len(rng)))
        page_number = page_number + 1
        sleep(randint(2, 10))

porn_movies = pd.DataFrame({
    'title' : title,
    'duration' : duration,
     'url' : link,
    'category' : category_movie
})

#Create and write data straight to the file w+, auto-rename'ing by category
with open("./bdsm-steak.csv", "w+") as file:
    file.write(porn_movies.to_csv())
#porn_movies.to_csv("./porn_hd.csv")