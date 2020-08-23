from selenium.webdriver.common.by import By
from utility_functions import amazon_data_processor
from base import drivers
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

amazonlocators = locators.amazon_locators()
class amazon(drivers.configure_dirvers):
    def __init__(self):
        super().__init__()

    def amazon(self):
        wait = WebDriverWait(self.chrome_driver, 10)
        self.chrome_driver.get(amazonlocators.main_link)
        self.chrome_driver.find_element_by_id(amazonlocators.search_bar).send_keys('Apple iPhone XR (64GB)')
        self.chrome_driver.find_element_by_css_selector(amazonlocators.search_button).click()
        try:
            table_data = wait.until(EC.presence_of_element_located((By.XPATH, amazonlocators.data_table)))
        except:
            table_data = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, amazonlocators.data_table_backup)))
        price = (amazon_data_processor.amazon_data_processor(table_data.text).process())
        print(price)
        return price

