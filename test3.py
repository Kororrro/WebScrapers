
# import requests
import time
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

element_list = []

service = Service(GeckoDriverManager().install())

for page in range(1,3):
    driver = webdriver.Firefox(options=options)

    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D"
    driver.get(url)
    time.sleep(2)  # Optional wait to ensure page loads

    # Extract product details
    titles = driver.find_elements(By.CLASS_NAME, "title")
    prices = driver.find_elements(By.CLASS_NAME, "price")
    descriptions = driver.find_elements(By.CLASS_NAME, "description")
    ratings = driver.find_elements(By.CLASS_NAME, "ratings")

    # Store results in a list
    for i in range(len(titles)):
        element_list.append([
            titles[i].text,
            prices[i].text,
            descriptions[i].text,
            ratings[i].text
        ])

    driver.quit()

# Display extracted data
for row in element_list:
    print(row)


# res = requests.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")
# soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())

# driver = webdriver.Firefox()
