from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.procyclingstats.com/rider/greg-van-avermaet")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
name = soup.find_all('title', limit=1)


for name in name:
    print(name.text)


