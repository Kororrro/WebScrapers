from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

"""
Write to file a list of posts on a reddit subreddit
"""

element_list = []

try:
    f = open("./links.txt", "w")
except:
    f = open("./links.txt", "x")

# Set up Chrome options (optional)
options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use a proper Service object
service = Service(GeckoDriverManager().install())

# for page in range(1, 5):
    # Initialize driver properly
driver = webdriver.Firefox(options=options, service=service)

    # Load the URL
url = f"https://www.reddit.com/r/webscraping/"
driver.get(url)
time.sleep(2)  # Optional wait to ensure page loads

# Extract product details
titles = driver.find_elements(By.CLASS_NAME, "absolute")
# prices = driver.find_elements(By.CLASS_NAME, "price")
# descriptions = driver.find_elements(By.CLASS_NAME, "description")
# ratings = driver.find_elements(By.CLASS_NAME, "ratings")

# Store results in a list
for i in range(len(titles)):
    if titles[i].text != '':
        element_list.append([
            titles[i].text,
            titles[i].get_attribute("href")
        # prices[i].text,
        # descriptions[i].text,
        # ratings[i].text
        ])

# element_list.remove('')
driver.quit()

# Display extracted data
for row in element_list:
    for i in row:
        f.write(i + ": ")
    f.write("\n")

