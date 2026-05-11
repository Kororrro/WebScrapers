import time
import requests
from bs4 import BeautifulSoup as BS

DoWrite = 0
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

def scrapeOLX(url, headers):
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BS(resp.text, 'html.parser')
    title = ""
    link_list = []
    for article in soup.select("div.css-u2ayx9"):
        link_tag = article.find("a")
        link = link_tag["href"]

    print(title)


# scrapeOLX(url=(url_list[2] + f"1"), headers=headers)
scrapeOLX(url=(url_list[2]), headers=headers)

if(DoWrite == 1):
    try:
        f = open("./links.txt", "w")
    except:
        f = open("./links.txt", "x")
    h=0
    # Write extracted data
    for row in text_list:
        f.write(f"Ogłoszenie:\n{row[0]}\nLink:\n{links_list[h]}\n")
        h+=1

if(DoPrint == 1):
    h = 0
    for row in text_list:
        print(f"\nOgłoszenie:\n{row[0]}")
        print(f"Link:\n{links_list[h]}")
        h += 1
