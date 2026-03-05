import scrapers
import requests
from bs4 import BeautifulSoup
# driver = scrapers.initialize()
# driver.get("https://www.reddit.com/")
sites = [
    "https://wpopole.pl/firmy/puby-opole"
]

try:
    f= open("oferty.txt", "w")
except:
    f= open("oferty.txt", "x")

for site in sites:
    f.write(site + " \n")
    res = requests.get(site)
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.find('div', class_='entry-content')
    if content:
        for para in content.find_all('p'):
            f.write(para.text.strip() + "\n")
    else:
        print("No article content found.")
    f.write("\n")    