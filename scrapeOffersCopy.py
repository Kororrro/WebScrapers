import time
import re
import requests
from bs4 import BeautifulSoup as BS
import logging
import sys

EXEC_TYPE = sys.argv[1]
DoWrite = 1
DoPrint = 0

url_list =[
    f"https://useme.com/pl/jobs/category/programowanie-i-it,35/?page=",
    f"https://www.pracuj.pl/praca/opole;wp?rd=0&et=1%2C17%2C2&pn=",
    f"https://www.olx.pl/nieruchomosci/mieszkania/wynajem/opole/q-mieszkanie-na-wynajem/"
]
headers = {
    "User-Agent": "Personal Research Bot 1.0 (contact: maciejkorniak07@gmail.com)"
}

def scrapeUseme(url, headers):
    site = "https://www.useme.com"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BS(resp.text, 'html.parser')
    title = ""

    for article in soup.select("div.job__content"):
        text = article.get_text(separator="\n", strip=True)
        link_tag = article.find("a", href=True)
        link = link_tag["href"] if link_tag else ""

        title += f"{site}{link}\n{text}\n\n"
    print(title)
    if DoWrite == 1:
        try:
            f = open("./links.txt", "w")
        except:
            f = open("./links.txt", "x")
        f.write(output)

def scrapePracujPL(url, headers):
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BS(resp.text, 'html.parser')
    title = ""

    for article in soup.select("a.tiles_cnb3rfy"):
        text = article.get("title")
        link = article.get("href")

        title += f"{link}\n{text}\n\n"
    print(title)
    if DoWrite == 1:
        try:
            f = open("./links.txt", "w")
        except:
            f = open("./links.txt", "x")
        f.write(output)

def scrapeOLX(url, headers):
    site = "https://www.olx.pl"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BS(resp.text, 'html.parser')
    title = ""
    link_list = []

    for article in soup.select("div.css-u2ayx9"):
        link_tag = article.find("a")
        link = link_tag["href"]
        if link.startswith("https://"):
            continue
        print(f"Appending {site}{link}")
        link_list.append(f"{site}{link}")
        

    print(link_list)
    output = ""
    for i in link_list:
        print(f"Trying to access {i}")
        offer = requests.get(url=i, headers=headers, timeout=30)
        offer.raise_for_status()
        soup = BS(offer.text, 'html.parser')
        
        title = soup.select_one("h4.css-1hd136p").get_text()
        price = soup.select_one("h3.css-yauxmy").get_text()
        description = soup.select_one("div.css-1rkcfco").get_text()

        # Write extracted data
        print(f"Adding new data to output: \n{title}\n{price}")
        output += f"{i}\n{title}\n{price}\n\n{description}\n\n"
    if DoWrite == 1:
        try:
            f = open("./links.txt", "w")
        except:
            f = open("./links.txt", "x")
        f.write(output)

match EXEC_TYPE:
    case "zlecenia":
        for i in range(1,6):
            scrapeUseme(url=(url_list[0] + f"{i}"), headers=headers)
    case "praca":
        for i in range(1,6):
            scrapePracujPL(url=(url_list[1] + f"{i}"), headers=headers)
    case "mieszkania":
        for i in range(1,6):
            scrapeOLX(url=(url_list[2] + f"{i}"), headers=headers)
        

if(DoPrint == 1):
    h = 0
    for row in text_list:
        print(f"\nOgłoszenie:\n{row[0]}")
        print(f"Link:\n{links_list[h]}")
        h += 1
