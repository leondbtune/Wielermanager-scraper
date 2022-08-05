from Rider import Rider
from asyncio.windows_events import NULL
import enum
from ntpath import join
from operator import contains
from bs4 import BeautifulSoup
import requests
import numpy as np
import csv

page_to_scrape = requests.get("https://www.procyclingstats.com/races.php?year=2022&circuit=1&class=&filter=Filter")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
winner = soup.select('a[href^="rider/"]')

scraper = requests.get("https://www.procyclingstats.com/races.php?year=2022&circuit=26&class=&filter=Filter")
soup2 = BeautifulSoup(scraper.text, "html.parser")
winner2 = soup2.select('a[href^="rider/"]')



race = []

for winner in winner:
    if winner.text != "":
        race.append(winner.find_previous("a")['href'])
    
for k in winner2:
    if k.text != "":
        race.append(k.find_previous("a")['href'])

site = []
test_list = ['tour', 'giro', 'nice', 'adriatico', 'volta','dauphine', 'itzulia', 'vuelta', 'jours', 'boucles' ]
for nr in race:
    res = [ele for ele in test_list if(ele in nr)]
    if res:
        pass
    else:
        site.append("https://www.procyclingstats.com/" + nr)
   
objects = []
for site in site:
    page_scrape = requests.get(site)
    soep = BeautifulSoup(page_scrape.text, "html.parser")
    riders = soep.select('a[href^="rider/"]')
    result = []
    points = []
    combined = []
    index = 0
    for riders in riders:
        result.append(riders.text)
        points.append("0" if riders.find_next("td").find_next("td").find_next("td").text == "" else riders.find_next("td").find_next("td").find_next("td").text)
        if np.array(objects).size == 0:
            rider = Rider(result[index], result[index], result[index])
            rider.add_general_points(int(points[index]))
            objects.append(rider)
        else:
            for each in objects:
                if each.name == result[index]:
                    each.add_general_points(int(points[index]))
                    
                else:
                    rider = Rider(result[index], result[index], result[index])
                    rider.add_general_points(int(points[index]))
                    objects.append(rider)
        index += 1
        
    

   
newlist = sorted(objects, key=lambda x: x.general_points, reverse=True)

file = open('rider.csv', newline='')
csvreader = csv.reader(file)
list = list(csvreader)

rows = []

for item in list:
    for i in item:
        rows.append(i.split(';'))

index = 0

for j in newlist:
    index += 1
    if index > 100:
        break
    else:
        for row in rows:
            if (j.name).startswith(row[1]):
                j.add_team(row[0])
                j.add_value(row[2])
                break
            else:
                pass

for item in newlist:
    if item.name == item.team:
        item.add_team("?")
        item.add_value("?")
    else:
        pass

index = 0
for riders in newlist:  
    print(riders.name, riders.general_points, riders.team, riders.value)
    index += 1
    if index > 100:
        break  