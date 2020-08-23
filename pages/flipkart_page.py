from selenium.webdriver.common.by import By
from utility_functions import flipkart_data_processor
from base import drivers
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

flipkartlocators = locators.flipkart_locators()


class flipkart_class(drivers.configure_dirvers):
    def __init__(self):
        super().__init__()

    def flipkart(self):
        wait = WebDriverWait(self.chrome_driver, 10)
        self.chrome_driver.get(flipkartlocators.main_link)
        element = wait.until(EC.presence_of_element_located((By.XPATH, flipkartlocators.close_button)))
        element.click()
        self.chrome_driver.find_element_by_css_selector(flipkartlocators.search_bar).send_keys('Apple iPhone XR (64GB)')
        self.chrome_driver.find_element_by_css_selector(flipkartlocators.search_button).click()

        table_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, flipkartlocators.data_table)))
        price = flipkart_data_processor.flipkart_data_processor(table_data.text).process()
        print(price)
        return price

    def flipkart_short_cut(self):
        wait = WebDriverWait(self.chrome_driver, 10)
        self.chrome_driver.get(flipkartlocators.short_cut_link)
        table_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, flipkartlocators.data_table)))
        price = (flipkart_data_processor.flipkart_data_processor(table_data.text).process())
        print(price)
        return price
