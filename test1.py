from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import scrapers
import time

"""
Write to file a list of posts on a reddit subreddit
"""
DoWrite = 0
DoPrint = 1
element_list = []

driver = scrapers.initialize(["no-sandbox","disable-dev-shm-usage"])

url = f"https://www.reddit.com/r/webscraping/"
driver.get(url)
time.sleep(2)  # Optional wait to ensure page loads
driver.refresh()

# Extract product details
titles = driver.find_elements(By.CLASS_NAME, "absolute")

# Store results in a list
for i in range(len(titles)):
    if titles[i].text != '':
        print("getting elements")
        element_list.append([
            titles[i].text,
            titles[i].get_attribute("href")
        ])
# element_list.remove('')
# driver.quit()

if(DoWrite == 1):
    try:
        f = open("./links.txt", "w")
    except:
        f = open("./links.txt", "x")
    # Write extracted data
    for row in element_list:
        for i in row:
            print("%s: ", i)
            f.write(i + ": ")
        f.write("\n")

if(DoPrint == 1):
    for row in element_list:
        for i in row:
            print("%s: " % i)