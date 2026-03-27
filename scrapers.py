from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
def initialize(args=[]):
    options = webdriver.FirefoxOptions()
    for el in args:
        options.add_argument(f"--{el}")
        # print(f"--{el}")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(options=options,service=service)
    return driver

def findAndClick(site,arg,tag):
    elems = site.find_elements(getattr(By, arg), f"{tag}")
    print(elems)
    for el in range(len(elems)):
        try:
            elems[el].click()
            print("element clicked")
        except:
            continue
    