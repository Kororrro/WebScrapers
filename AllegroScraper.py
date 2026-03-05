import time
import requests
from scrapers import initialize
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

"""
Idea:  pick a single shopping website, search for a custom 
       phrase and return a number of positions with their:
       names, prices, links and additional cool information
"""

def authwait(driver):
    if elem.id:
        return 1
    else:
        return 0

try:
    f= open("allegroList.txt", "w")
except:
    f= open("allegroList.txt", "x")

filtList = []
options = webdriver.FirefoxOptions()
service = Service(GeckoDriverManager().install())

prompt = input("Co chcesz wyszukać?\n")
url = f"https://allegro.pl/listing?string={prompt}"
driver = webdriver.Firefox(service=service)
# res = requests.get(url)
# soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())
driver.get(url)
time.sleep(20)
# elem = driver.find_element(By.TAG_NAME, "div")
# print(elem)

# while(authwait(driver) == 1):
#     time.sleep(3)

listings = driver.find_elements(By.CLASS_NAME, "mr3m_1")

for i in range(len(listings)):
    print("pętla " + i)
    try:
        filtList.append([
            listings[i].text,
            listings[i].get_attribute("aria-label")
        ])
    except:
        continue

for i in filtList:
    for j in i:
        try:
            f.write(j)
        except:
            continue
    f.write("\n")