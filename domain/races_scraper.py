from asyncio.windows_events import NULL
import enum
from ntpath import join
from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.procyclingstats.com/races.php?year=2022&circuit=1&class=&filter=Filter")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
winner = soup.select('a[href^="rider/"]')



race = []

for winner in winner:
    if winner.text != "":
        race.append(winner.find_previous("a")['href'])
    
print(race)
site = []
for nr in race:
    site.append("https://www.procyclingstats.com/" + nr)
   

#for site in site:
#    page_scrape = requests.get(site)
#    soep = BeautifulSoup(page_scrape.text, "html.parser")
#    riders = soep.select('a[href^="rider/"]')
#    result = []
#    points = []
#    combined = []
#    index = 0
# #   for riders in riders:
#        result.append(riders.text)
#        points.append(riders.find_next("td").find_next("td").find_next("td").text)
#        
#    
#
#    for point in points:
#        combined.append(result[index] + " " + point)
#        index += 1
# 
#
 #   print(combined)
    
   