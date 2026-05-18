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
    "olx" : f"https://www.olx.pl/nieruchomosci/mieszkania/wynajem/opole/q-mieszkanie-na-wynajem/",
    "olx-praca-1" : f"https://www.olx.pl/praca/opole/?search%5Bfilter_enum_agreement%5D%5B0%5D=zlecenie",
    "olx-praca-2": f"https://www.olx.pl/praca/opole/?search%5Bfilter_enum_type%5D%5B0%5D=fulltime&search%5Bfilter_enum_agreement%5D%5B0%5D=zlecenie",
    "olx_test" : f"https://www.olx.pl/praca/"
}
headers = {
    "User-Agent": "Personal Research Bot 1.0 (contact: maciejkorniak07@gmail.com)"
}

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

def scrapeOLX(url, headers, f, tags):
    site = "https://www.olx.pl"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BS(resp.text, 'html.parser')
    title = ""
    link_list = []

    print(tags[0])

    for article in soup.select(f"{tags[0]}"):
        print("This is getting executed")
        link_tag = article.find("a", None ,True)
        print(link_tag)
        link = link_tag["href"]
        print(link)
        if link.startswith("https://"):
            continue
        print(f"Appending list of links")
        link_list.append(f"{site}{link}")
        

    print(link_list)
    output = ""
    for i in link_list:
        print(f"{Bcolors.OKGREEN}Trying to access{Bcolors.ENDC} {i}")
        offer = requests.get(url=i, headers=headers, timeout=30)
        offer.raise_for_status()
        soup = BS(offer.text, 'html.parser')
        title = ""

        for j in tags:
            if j == tags[0]: 
                continue
            try:
                title += soup.select_one(j).get_text("\n") + "\n"
                print(f"{Bcolors.OKBLUE}Adding new data to output:{Bcolors.ENDC}\n{title}")
                
            except:
                print(f"{Bcolors.WARNING}Something went wrong while adding text")
                input("Proceed?\t")
        
        # Write extracted data
        output += f"{i}\n\n{title}\n\n"
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
        try:
            pracuj_file = open("linkipraca.txt", "x")
        except:
            pracuj_file = open("linkipraca.txt", "w")
        tags = [
            "div.css-qnyeki",
            "h1.css-wzfqzc",
            "div.css-1he1sjz"
        ]
        mieszkania_tagi = [
            "css-u2ayx9"
        ]
        
        scrapeOLX(url_list[f"olx_test"], headers, pracuj_file, tags)
        # scrapeOLX(url_list[f"olx-praca-1"], headers, pracuj_file, tags)
        # scrapeOLX(url_list[f"olx-praca-2"], headers, pracuj_file, tags)

if(DoPrint == 1):
    h = 0
    for row in text_list:
        print(f"\nOgłoszenie:\n{row[0]}")
        print(f"Link:\n{links_list[h]}")
        h += 1
