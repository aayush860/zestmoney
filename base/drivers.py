from selenium import webdriver
import os

class configure_dirvers:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        print(BASE_DIR+'/base/chromedriver')
        self.chrome_driver = webdriver.Chrome(BASE_DIR+'/base/chromedriver')

    def config_driver(self):
        self.chrome_driver.implicitly_wait(15)
        self.chrome_driver.get("https://www.google.in/")
        return self.chrome_driver

