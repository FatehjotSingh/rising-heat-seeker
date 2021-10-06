from selenium import webdriver as wd
from bs4 import BeautifulSoup as bou
import time
import requests
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(start_url)

soup = bou(page.text, 'html.parser')
start_table = soup.find_all('table')

templist = []

tablerows = start_table[4].find_all('tr')

for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]

    templist.append(row)
    
starnames =[]
distance =[]
mass =[] 
radius =[] 


for i in range(1,len(templist)):

    starnames.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])

df = pd.DataFrame((list(zip(starnames,distance,mass,radius))),columns=['starnames','distance','mass','radius'])
df.to_csv('dwarves.csv')