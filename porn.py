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
#categories = []

category = str(input("Category: "))
count_page = int(input("Count of pages: "))

title = []
duration = []
link = []

##################################################################
#Category URL get:

category_url = requests.get("https://bdsmstreak.com/categories")
category = BeautifulSoup(category_url.text,'html.parser')

a_category = category.select('a[href*="category"]')

for link in a_category:
    print("https://bdsmstreak.com" + link.get("href"))
###################################################################
#Range of pages:

#pages = np.arange(1,count_page,1)
#Looping through each page
#Request(URL) + 'html_soup' + 'porn_link'

#Counting pages while looping:
page_number = 1

for page in range(1,count_page,1):


    #Requesting

    print("Requesting")

    page = requests.get("https://bdsmstreak.com/category/"+category+"?page=" + str(page))


    soup = BeautifulSoup(page.text, 'html.parser')

    porn = soup.findAll('a', class_='vidlink')

    durations = soup.findAll("div", class_="duration")

    titles = soup.findAll("div", class_="videotitle")

    sleep(randint(2,10))

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

    print("Current page : " + str(page_number) + " / " + count_page)
    page_number = page_number + 1

porn_movies = pd.DataFrame({
    'title' : title,
    'duration' : duration,
    'url' : link,
})

#Create and write data straight to the file w+, auto-rename'ing by category

with open("./data/porn_{0}.csv".format(category), "w+") as file:
    file.write(porn_movies.to_csv())

#porn_movies.to_csv("./porn_hd.csv")