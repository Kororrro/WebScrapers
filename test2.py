import scrapers
import requests
from bs4 import BeautifulSoup

try:
    f= open("oferty.txt", "w")
except:
    f= open("oferty.txt", "x")

sites=[]
for i in range(1, 6):
    sites.append(f"https://useme.com/pl/jobs/category/programowanie-i-it,35/?page={i}")


for site in sites:
    # f.write(site + " \n")
    res = requests.get(site)
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.find('div', class_='entry-content')
    print(soup)
    input("proceed")
    print(content)
    input()
    if content:
        for para in content.find_all('div.job__content'):
            f.write(para.text.strip() + "\n")
    else:
        print("No article content found.")
    f.write("\n")    