import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager

def autologin(driver, number, myPassword):
    LIST = []
    elems = driver.find_elements(By.CLASS_NAME, "html-div")
    for el in range(len(elems)):
        # LIST.append([
        #     elems[el].text,
        #     elems[el].id
        # ])
        if(elems[el].text == 'Decline optional cookies'):
            elems[el].click()
            print("Declining cookies")
    #Now I got past optional cookies ^^
    mail = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    button = driver.find_element(By.ID, "loginbutton")
    print("Entering credentials and logging in")
    mail.send_keys(number)
    password.send_keys(myPassword)
    button.click()

def chats(driver):
    messages = driver.find_elements(By.CLASS_NAME,"x78zum5")

    for elem in range(len(messages)):
        elemList.append([
            messages[elem].text,
            messages[elem].get_attribute("href")
        ])

    for el in elemList:
        print(el)


elemList = []
number = ""
password = ""
loginurl= "https://www.facebook.com/login.php"

options = webdriver.FirefoxOptions()
# options.add_argument("--P Default")
service = Service(GeckoDriverManager().install())

driver = webdriver.Firefox(options=options, service=service)

authurl = f"https://www.facebook.com/two_step_verification/authentication/"
url = f"https://www.facebook.com/messages/"
driver.get(url)
time.sleep(2)

if loginurl in driver.current_url:
    print("Executing autologin")
    autologin(driver, number, password)
    time.sleep(2)
while (True):
    if authurl in driver.current_url:
        print("Waiting for authentication")
        time.sleep(5)
    else:
        break
chats(driver)