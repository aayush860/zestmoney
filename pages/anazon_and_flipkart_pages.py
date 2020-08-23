from selenium.webdriver.common.by import By
from utility_functions import flipkart_data_processor, amazon_data_processor
from base import drivers
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver = drivers.configure_dirvers().config_driver()
wait = WebDriverWait(chrome_driver, 10)
amazonlocators = locators.amazon_locators()
flipkartlocators = locators.flipkart_locators()


class login_page(drivers.configure_dirvers):
    def __init__(self):
        super().__init__()

    def amazon(self):
        chrome_driver.find_element_by_id(amazonlocators.search_bar).send_keys('Apple iPhone XR (64GB)')
        chrome_driver.find_element_by_css_selector(amazonlocators.search_button).click()
        try:
            table_data = wait.until(EC.presence_of_element_located((By.XPATH, amazonlocators.data_table)))
        except:
            table_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, amazonlocators.data_table_backup)))
        return amazon_data_processor.amazon_data_processor(table_data.text).process()


    def flipkart(self):
        chrome_driver.get("https://www.flipkart.com/")
        element = wait.until(EC.presence_of_element_located((By.XPATH, flipkartlocators.close_button)))
        element.click()
        chrome_driver.find_element_by_css_selector(flipkartlocators.search_bar).send_keys('Apple iPhone XR (64GB)')
        chrome_driver.find_element_by_css_selector(flipkartlocators.search_button).click()

        table_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, flipkartlocators.data_table)))
        return flipkart_data_processor.flipkart_data_processor(table_data.text).process()


    def flipkart_short_cut(self):
        chrome_driver.get("https://www.flipkart.com/search?q=Apple%20iPhone%20XR%20%2864GB%29&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
        table_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, flipkartlocators.data_table)))
        return flipkart_data_processor.flipkart_data_processor(table_data.text).process()
