from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import scrapers
import time

DoWrite = 1
DoPrint = 0
links_list = []
text_list = []

driver = scrapers.initialize(["no-sandbox","disable-dev-shm-usage"])

if(DoWrite == 1):
    try:
        f = open("./links.txt", "w")
    except:
        f = open("./links.txt", "x")

for i in range(1,6):
    url = f"https://useme.com/pl/jobs/category/programowanie-i-it,35/?page={i}"
    driver.get(url)
    driver.refresh()
    time.sleep(20)  # Optional wait to ensure page loads
    # input("Proceed? ")

    # Extract product details
    titles = driver.find_elements(By.CLASS_NAME, "job__content")

    # Store results in a list
    for i in range(len(titles)):
        if titles[i].text != '':
            print("getting elements")
            text_list.append([
                titles[i].text
            ])
            links_list.append(
                titles[i].find_element(By.TAG_NAME, "a").get_attribute("href")
            )
    h = 0
    if(DoWrite == 1):
        # Write extracted data
        for row in text_list:
            f.write(f"Ogłoszenie:\n{row[0]}\nLink:\n{links_list[h]}\n")
            h+=1

    h = 0
    if(DoPrint == 1):
        for row in text_list:
            print(f"\nOgłoszenie:\n{row[0]}")
            print(f"Link:\n{links_list[h]}")
            h += 1


# element_list.remove('')
driver.quit()

# if(DoWrite == 1):
#     try:
#         f = open("./links.txt", "w")
#     except:
#         f = open("./links.txt", "x")
#     # Write extracted data
#     for row in text_list:
#         for i in row:
#             print("%s: ", i)
#             f.write(i + ": ")
#         f.write("\n")

# h = 0
# if(DoPrint == 1):
#     for row in text_list:
#         print(f"\nOgłoszenie:\n{row[0]}")
#         print(f"Link:\n{links_list[h]}")
#         h += 1

# print(f"TEXT_LIST:\n{text_list}")
# print(f"LINKS_LIST:\n{links_list}")