from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class configure_dirvers:
    def __init__(self):
        self.chrome_driver = webdriver.Chrome("/Users/aayushbhargava/Downloads/chromedriver")

    def config_driver(self):
        self.chrome_driver.implicitly_wait(15)
        self.chrome_driver.get("https://www.google.in/")
        return self.chrome_driver

