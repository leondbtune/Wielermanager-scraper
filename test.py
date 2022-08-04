from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.procyclingstats.com/races.php?year=2022&circuit=1&class=&filter=Filter")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
winner = soup.select('a[href^="rider/"]')



race = []

for winner in winner:
    if winner.text != "":
        race.append(winner.find_previous("a")['href'])
    
index = 0
site = []
for nr in race:
    site.append("https://www.procyclingstats.com/" + nr)
   

print(site)