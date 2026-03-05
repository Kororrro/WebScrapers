from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
def initialize():
    options = webdriver.FirefoxOptions()
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    return driver