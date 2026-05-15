import time
import re
import requests
from bs4 import BeautifulSoup as BS
import logging
import sys

if len(sys.argv) == 1:
    EXEC_TYPE = input("What action would you like to perform?\n")
else:
    EXEC_TYPE = sys.argv[1]

DoWrite = 1
DoPrint = 0

url_list ={
    "useme" : f"https://useme.com/pl/jobs/category/programowanie-i-it,35/?page=",
    "pracujpl-1" :f"https://www.pracuj.pl/praca/opole;wp?rd=0&et=1%2C17%2C2&pn=",
    "pracujpl-2" : f"https://it.pracuj.pl/praca/opole;wp?rd=0&et=17&tc=2",
    "olx" : f"https://www.olx.pl/nieruchomosci/mieszkania/wynajem/opole/q-mieszkanie-na-wynajem/"
}
headers = {
    "User-Agent": "Personal Research Bot 1.0 (contact: maciejkorniak07@gmail.com)"
}

def scrapeUseme(url, headers, f):
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
        f.write(title)

def scrapePracujPL(url, headers, f):
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
        f.write(title)

def scrapeOLX(url, headers, f):
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
        print(f"Appending list of links")
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
        print(f"Adding new data to output: \n{title}")
        output += f"{i}\n{title}\n{price}\n\n{description}\n\n"
    if DoWrite == 1:
        f.write(output)

match EXEC_TYPE:
    case "zlecenia":
        useme_file = None
        if DoWrite == 1:
            try:
                useme_file = open("./useme_file.txt", "w")
            except:
                useme_file = open("./useme_file.txt", "x")
        for i in range(1,6):
            scrapeUseme(url=(url_list["useme"] + f"{i}"), headers=headers, f=useme_file)

    case "praca":
        pracuj_file = None
        if DoWrite == 1:
            try:
                pracuj_file = open("./pracuj_file.txt", "w")
            except:
                pracuj_file = open("./pracuj_file.txt", "x")
        for i in range(1,6):
            scrapePracujPL(url=(url_list["pracujpl-1"] + f"{i}"), headers=headers, f=pracuj_file)

    case "mieszkania":
        olx_file = None
        if DoWrite == 1:
            try:
                olx_file = open("./olx_file.txt", "w")
            except:
                olx_file = open("./olx_file.txt", "x")
        for i in range(1,6):
            scrapeOLX(url=(url_list["olx"] + f"{i}"), headers=headers, f=olx_file)

    case "all":
        useme_file = None
        pracuj_file = None
        olx_file = None
        if DoWrite == 1:
            try:
                useme_file = open("./useme_file.txt", "w")
                pracuj_file = open("./pracuj_file.txt", "w")
                olx_file = open("./olx_file.txt", "w")
            except:
                useme_file = open("./useme_file.txt", "x")
                pracuj_file = open("./pracuj_file.txt", "x")
                olx_file = open("./olx_file.txt", "x")
        for i in range(1,6):
            scrapeUseme(url=(url_list["useme"] + f"{i}"), headers=headers, f=useme_file)
            scrapePracujPL(url=(url_list["pracujpl-1"] + f"{i}"), headers=headers, f=pracuj_file)
            scrapeOLX(url=(url_list["olx"] + f"{i}"), headers=headers, f=olx_file)

    case "test":
        pracuj_file = open("linkipraca.txt", "x")
        for i in range(1,3):
            scrapePracujPL(url_list[f"pracujpl-{i}"], headers, pracuj_file)

if(DoPrint == 1):
    h = 0
    for row in text_list:
        print(f"\nOgłoszenie:\n{row[0]}")
        print(f"Link:\n{links_list[h]}")
        h += 1
